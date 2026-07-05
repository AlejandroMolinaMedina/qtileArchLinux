#!/bin/bash

# Directorio de fondos de pantalla
WALLPAPER_DIR="$HOME/.secrets/wallpapers"

# Seleccionar una imagen aleatoria (jpg, png, jpeg)
WALLPAPER=$(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \) | shuf -n 1)

# Establecer el fondo de pantalla usando feh
if [ -n "$WALLPAPER" ]; then
    feh --bg-fill "$WALLPAPER"
fi
