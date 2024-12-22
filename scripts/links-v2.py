

import os
import re
from pathlib import Path

def find_links(content):
    # Recherche des liens au format [[nom]] ou [[nom|affichage]]
    links = re.findall(r'\[\[([^\|\]]+)\]\]|\[\[([^\|\]]+)\|([^\]]+)\]\]', content)
    return links

def convert_link(link, relative_path):
    # Cas [[Nom du fichier]] sans ancre ni alias
    if link[0]:  
        file_part = link[0].split('#')[0]  # Prend la partie avant l'ancre #
        return f'[[{link[0]}]]', f'[{link[0]}]({relative_path}/{file_part}.md)', f'{file_part}.md'
    # Cas [[Nom du fichier|Texte affiché]]
    elif link[1] and link[2]:  
        file_part = link[1].split('#')[0]  # Prend la partie avant l'ancre #
        return f'[[{link[1]}|{link[2]}]]', f'[{link[2]}]({relative_path}/{file_part}.md)', f'{file_part}.md'
    return '', '', ''

def find_file(filename, search_directory):
    """Recherche récursive du fichier dans un répertoire."""
    for root, dirs, files in os.walk(search_directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Chemin du répertoire source
source_directory = "/mnt/data-1T/data/developpement-it/documentations/it/mk-docs/documentations_linux/docs"
base_target_directory = "/mnt/data-1T/data/developpement-it/documentations/it/mk-docs/documentations_linux/docs"
target_directory = os.path.join(base_target_directory, "obsidian_test")

# Créer le répertoire de destination s'il n'existe pas
if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Parcourir les fichiers Obsidian et copier avec remplacement des liens
obsidian_paths = ["/mnt/data-1T/data/developpement-it/documentations/it/obsidiann/Linux/03_PROJET"]

for obsidian_path in obsidian_paths:
    for root, dirs, files in os.walk(obsidian_path):
        for file in files:
            if file.endswith(".md"):
                src_filepath = os.path.join(root, file)
                target_filepath = os.path.join(target_directory, os.path.relpath(src_filepath, obsidian_path))
                target_file_dir = os.path.dirname(target_filepath)
                
                # Créer le répertoire cible s'il n'existe pas
                if not os.path.exists(target_file_dir):
                    os.makedirs(target_file_dir)

                # Lire le contenu du fichier source
                with open(src_filepath, 'r') as f:
                    content = f.read()
                
                # Trouver tous les liens dans le contenu
                links = find_links(content)
                
                # Remplacement des liens Obsidian par des liens MkDocs
                for link in links:
                    # Rechercher le fichier correspondant au lien
                    obsidian_link, mkdocs_link, filename = convert_link(link, "")
                    
                    # Recherche du fichier dans le répertoire source
                    found_file = find_file(filename, source_directory)
                    if found_file:
                        # Calculer le chemin relatif entre le fichier trouvé et la destination
                        relative_path = os.path.relpath(os.path.dirname(found_file), target_file_dir)
                        mkdocs_link = f'[{link[0] or link[2]}]({relative_path}/{filename})'
                        content = content.replace(obsidian_link, mkdocs_link)
                        print(f"Fichier à modifier : {src_filepath}")
                        print(f"Lien Obsidian : {obsidian_link}")
                        print(f"Lien MkDocs : {mkdocs_link}")
                        print(f"Chemin absolu du fichier source : {found_file}\n")
                    else:
                        # Afficher des informations en cas de fichier introuvable
                        print(f"Fichier introuvable pour : \n{'link':<20}: {link}\n{'obsidian_link':<20}: {obsidian_link}\n{'mkdocs_link':<20}: {mkdocs_link}\n{'convert_link':<20}: {filename}\n")

                # Enregistrer le contenu avec les liens convertis
                with open(target_filepath, 'w') as f:
                    f.write(content)
                print(f"Fichier copié et liens convertis : {target_filepath}")
