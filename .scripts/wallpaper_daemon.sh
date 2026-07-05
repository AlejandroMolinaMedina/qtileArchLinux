#!/bin/bash

# Directorio de fondos de pantalla
WALLPAPER_DIR="$HOME/.secrets/wallpapers"

# Bucle infinito para rotar fondos de pantalla
while true; do
    # Obtener lista de imágenes, mezclar aleatoriamente y iterar
    mapfile -t wallpapers < <(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \) | shuf)
    
    for wallpaper in "${wallpapers[@]}"; do
        feh --bg-fill "$wallpaper"
        # Dormir 5 minutos (300 segundos)
        sleep 300
    done
done
