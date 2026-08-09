# Qtile Arch Linux Modular Configuration

![Qtile](https://img.shields.io/badge/Qtile-v0.23+-blue?logo=qtile&logoColor=white)
![Arch Linux](https://img.shields.io/badge/Arch_Linux-Rolling-1793D1?logo=archlinux&logoColor=white)
![Modular](https://img.shields.io/badge/Architecture-Modular-green)

Una configuración de **Qtile** altamente personalizada, modularizada y moderna, diseñada específicamente para **Arch Linux** y compatible con **Fedora**. Este entorno está optimizado para maximizar el flujo de trabajo, la estética visual y la facilidad de mantenimiento a largo plazo mediante una arquitectura desacoplada.

## 🚀 Características Principales

*   **BarRotator (Barra inteligente)**: Optimización avanzada del espacio mediante la rotación cíclica de métricas críticas (brillo, volumen, red, batería).
*   **Gestión Dinámica de Grupos**: Sistema inteligente basado en `group_manager.py` que mapea aplicaciones automáticamente a escritorios específicos mediante `WM_CLASS`.
*   **Estética Pulida**: Integración de **Picom** (blur, sombras, esquinas redondeadas) y **Alacritty** para una experiencia visual cohesiva.
*   **Interactividad Gestual**: Soporte nativo para gestos en el touchpad mediante `libinput-gestures`.
*   **Arquitectura Modular**: Separación estricta de lógica, estilos y scripts de automatización para evitar archivos de configuración monolíticos.
*   **Auto-instalación**: Listas de paquetes categorizadas para despliegue rápido en sistemas Arch y Fedora.

## 📂 Estructura del Proyecto

```text
.
├── alacritty/              # Configuración del emulador de terminal
├── gestures/               # Configuración de libinput-gestures
├── modules/                # Lógica del core (BarRotator, widgets, funciones)
├── packageInstall/         # Scripts y listas de paquetes por distribución
├── picom/                  # Configuración del compositor
├── styles/                 # Definición de temas (Barra, colores)
├── utils/                  # Gestión dinámica de grupos y utilidades
├── config.py               # Punto de entrada principal
└── COMMIT_CONVENTIONS.md   # Guía para el historial de cambios
```

## 🛠️ Guía de Inicio Rápido

### Requisitos Previos
1. Sistema base instalado (**Arch Linux** o **Fedora**).
2. `git` para clonar el repositorio.

### Instalación
1. Clona el repositorio en tu carpeta de configuración:
   ```bash
   git clone <URL_DEL_REPOSITORIO> ~/.config/qtile
   ```
2. Instala las dependencias según tu distribución:

   **Para Arch Linux:**
   ```bash
   sudo pacman -S --needed - < packageInstall/archLinux/pkglist.txt
   yay -S --needed - < packageInstall/archLinux/aurlist.txt
   ```

   **Para Fedora:**
   ```bash
   sudo dnf install -y $(cat packageInstall/fedora/pkglist.txt)
   ```

3. Reinicia tu sesión de X11 y selecciona **Qtile** desde tu gestor de inicio (display manager).

## 📋 Dependencias Clave

| Dependencia | Descripción |
| :--- | :--- |
| **Qtile** | Gestor de ventanas principal |
| **Picom** | Compositor para efectos visuales |
| **Alacritty** | Emulador de terminal acelerado por GPU |
| **libinput-gestures** | Soporte de gestos para touchpad |
| **brightnessctl** | Control de brillo del hardware |
| **Nerd Fonts** | Iconos y símbolos para la barra de estado |

## 🤝 Mantenimiento y Contribución

Este proyecto sigue convenciones estrictas para asegurar la claridad en el historial de cambios. Antes de realizar modificaciones, por favor consulta el archivo `COMMIT_CONVENTIONS.md`.

*   **Reportar errores:** Utiliza la sección de *Issues* para reportar comportamientos inesperados.
*   **Contribuciones:** Los *Pull Requests* son bienvenidos. Asegúrate de que los cambios sigan la estructura modular del proyecto y respeten el estándar de *commits* definido.

---
*Configuración mantenida bajo un flujo de trabajo modular y eficiente para entornos Linux avanzados.*