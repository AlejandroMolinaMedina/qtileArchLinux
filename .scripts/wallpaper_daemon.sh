#!/bin/bash

# Directorio de configuración
WALLPAPER_DIR="$HOME/.secrets/wallpapers"
# Log en tu carpeta personal para que no se borre
LOG_FILE="$HOME/.cache/wallpaper_daemon.log"

# Asegurar que el archivo de log exista
mkdir -p "$(dirname "$LOG_FILE")"
touch "$LOG_FILE"

echo "$(date): --- Iniciando demonio de fondos de pantalla ---" >> "$LOG_FILE"

# Evitar múltiples instancias
if pgrep -f "$(basename "$0")" | grep -v $$ > /dev/null; then
    echo "$(date): Ya existe una instancia corriendo. Cerrando." >> "$LOG_FILE"
    exit 0
fi

while true; do
    # Buscar archivos, mezclar y procesar de forma segura
    find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \) -print0 | shuf -z | while IFS= read -r -d '' wallpaper; do
        
        if [ -f "$wallpaper" ]; then
            echo "$(date): Estableciendo fondo: $wallpaper" >> "$LOG_FILE"
            # DISPLAY=:0 es necesario si lo ejecutas desde el autostart de Qtile
            DISPLAY=:0 feh --bg-fill "$wallpaper"
        else
            echo "$(date): Error: El archivo $wallpaper no es válido." >> "$LOG_FILE"
        fi
        
        sleep 300
    done
done