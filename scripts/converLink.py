import os
import re
import shutil
from pathlib import Path

# Chemins de base
source_directory = "/mnt/data-1T/data/developpement-it/documentations/it/mk-docs/documentations_linux/docs"
clone_directory = "/mnt/data-1T/data/developpement-it/documentations/it/mk-docs/documentations_linux/docs_clone"

# Étape 1 : Créer un clone du répertoire `docs`
if os.path.exists(clone_directory):
    shutil.rmtree(clone_directory)
shutil.copytree(source_directory, clone_directory)

# Fonction pour trouver et convertir les liens Obsidian
def find_and_convert_links(content, file_path):
    links = re.findall(r'\[\[([^\|\]]+)\]\]|\[\[([^\|\]]+)\|([^\]]+)\]\]', content)
    for link in links:
        if link[0]:  # Cas [[nom]]
            filename = link[0].split('#')[0]
            anchor = link[0].split('#')[1] if '#' in link[0] else ''
            display_text = filename
        elif link[1] and link[2]:  # Cas [[nom|affichage]]
            filename = link[1].split('#')[0]
            anchor = link[1].split('#')[1] if '#' in link[1] else ''
            display_text = link[2]
        else:
            continue
        
        # Chemin relatif du fichier cible
        target_file = find_file(filename, clone_directory)
        if target_file:
            relative_path = os.path.relpath(target_file, os.path.dirname(file_path))
            markdown_link = f"[{display_text}]({relative_path}{'#' + anchor if anchor else ''})"
            obsidian_link = f'[[{link[0]}]]' if link[0] else f'[[{link[1]}|{link[2]}]]'
            content = content.replace(obsidian_link, markdown_link)
        else:
            with open("conversion_errors.log", "a") as error_log:
                error_log.write(f"Link not found: {target_file} in file {file_path}\n")

    return content

# Fonction pour trouver un fichier par son nom
def find_file(filename, search_directory):
    for root, _, files in os.walk(search_directory):
        if filename + ".md" in files:
            return os.path.join(root, filename + ".md")
    return None

# Étape 2 : Parcourir `docs_clone` pour remplacer les liens Obsidian
for root, _, files in os.walk(clone_directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                content = f.read()
            content = find_and_convert_links(content, file_path)
            with open(file_path, "w") as f:
                f.write(content)
