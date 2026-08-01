#!/bin/bash

# Define el modo
MODE=$1

# Si no se pasa argumento, detectar y alternar
if [ -z "$MODE" ]; then
    CURRENT_SCHEME=$(gsettings get org.gnome.desktop.interface color-scheme)
    if [ "$CURRENT_SCHEME" == "'prefer-dark'" ]; then
        MODE="light"
    else
        MODE="dark"
    fi
fi

if [ "$MODE" == "dark" ]; then
    # Aplicar modo oscuro para GTK
    gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
    gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
    
    # Solo intentar modificar qt6ct si el archivo existe
    if [ -f "$HOME/.config/qt6ct/qt6ct.conf" ]; then
        sed -i 's/color_scheme=.*/color_scheme=Dark/g' "$HOME/.config/qt6ct/qt6ct.conf"
    fi

elif [ "$MODE" == "light" ]; then
    # Aplicar modo claro para GTK
    gsettings set org.gnome.desktop.interface color-scheme 'default'
    gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'
    
    if [ -f "$HOME/.config/qt6ct/qt6ct.conf" ]; then
        sed -i 's/color_scheme=.*/color_scheme=Light/g' "$HOME/.config/qt6ct/qt6ct.conf"
    fi
else
    echo "Uso: ./set_mode.sh [dark|light]"
fi
