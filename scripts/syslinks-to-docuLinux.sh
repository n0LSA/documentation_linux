#!/bin/bash


######################################################################
#
# SCRIPTS A MODIFIER AVANT UTILISATION
#
# modifier la variable "destDir" suivant le repertoir ou la créations de liens doit etre faite via $1
# FONCTIONNE SUR 1 SEUL NIVEAU DE SOUS-DOSSIER
#
######################################################################


# Vérifie si l'option --dry-run est présente
dry_run=false
if [[ "$1" == "--dry-run" ]]; then
    dry_run=true
    shift  # Enlève --dry-run des arguments
    echo "DRY RUN"
fi

# Vérifie que l'emplacement du dossier est fourni
if [[ -z "$1" ]]; then
    echo "Usage: $0 [--dry-run] <dossier>"
    exit 1
fi

directory=$1

# Vérifie que le dossier existe
if [[ ! -d "$directory" ]]; then
    echo "Erreur : le dossier '$directory' n'existe pas."
    exit 1
fi

# Parcourir tous les fichiers du dossier
find "$directory" -type f ! -type l | while IFS= read -r symlink_path; do
    # Vérifier si le lien symbolique est brisé
    if [ -e "$symlink_path" ]; then
        
        # chemin complet ver le fichier a remplacer par un lien symbolique
        source=$(realpath "$symlink_path")
        
        # dirname pour récupérer le repertoir relatif du fichier  via $1 
        dirName=$(dirname "$symlink_path")
        
        # nom du dossier ou se trouve le fichier
        subDir=$(echo "$dirName" | sed "s|$1/||g")

        # repertoir de destination
        destDir="/mnt/data-1T/data/developpement-it/documentations/it/mk-docs/documentations_linux/docs/commandes-de-base/$subDir"
        if $dry_run; then
            echo "symlink_path: $symlink_path"
            echo "basename:     $(basename "$symlink_path")"
            echo "source:       $source"
            echo "dirName:      $dirName"
            echo "subDir:       $subDir"
            echo "destDir:      $destDir - $(stat $destDir > /dev/null 2>&1 && echo "existe" || echo "n'existe pas")" 
        fi
        if [ -d "$destDir" ]; then 
            finalPath="$destDir/$(basename "$symlink_path")" 
            if $dry_run; then
                echo "finalPath:    $finalPath - $(stat $finalPath > /dev/null 2>&1 && echo "existe" || echo "n'existe pas")"
            fi
            if [ -e "$source" ]; then
                if ! $dry_run; then
                    echo "$symlink_path "
                    echo "      $source"
                    echo "      $finalPath"
                    mv "$source" "$finalPath"
                    ln -s "$finalPath" "$source"
                fi
            fi

        fi

        echo ""
    fi
done