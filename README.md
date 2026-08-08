# Qtile Arch Linux Modular Configuration

![Qtile](https://img.shields.io/badge/Qtile-v0.23+-blue?logo=qtile&logoColor=white)
![Arch Linux](https://img.shields.io/badge/Arch_Linux-Rolling-1793D1?logo=archlinux&logoColor=white)
![Modular](https://img.shields.io/badge/Architecture-Modular-green)

Una configuración de **Qtile** altamente personalizada, modularizada y moderna, diseñada específicamente para **Arch Linux**. Este entorno está optimizado para maximizar el flujo de trabajo, la estética visual y la facilidad de mantenimiento a largo plazo.

## 🚀 Características Principales

*   **BarRotator (Barra inteligente)**: Optimización avanzada del espacio mediante la rotación cíclica de métricas críticas (brillo, volumen, red, batería).
*   **Gestión Dinámica de Grupos**: Sistema inteligente que mapea aplicaciones automáticamente a escritorios específicos mediante `WM_CLASS`, con reordenamiento numérico dinámico.
*   **Estética Pulida**: Integración de **Picom** (blur, sombras, esquinas redondeadas) y **Alacritty** para una experiencia visual cohesiva y minimalista.
*   **Interactividad Gestual**: Soporte nativo para gestos en el touchpad mediante `libinput-gestures`.
*   **Arquitectura Modular**: Separación estricta de lógica, estilos, gestión de grupos y scripts de automatización para evitar archivos de configuración monolíticos.
*   **Auto-instalación**: Listas de paquetes categorizadas para despliegue rápido en Arch Linux y Fedora.

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
1. Tener instalado un sistema base con **Arch Linux** (o Fedora).
2. Contar con `git` para clonar el repositorio.

### Instalación
1. Clona el repositorio en tu carpeta de configuración:
   ```bash
   git clone <URL_DEL_REPOSITORIO> ~/.config/qtile
   ```
2. Instala las dependencias necesarias según tu distribución:
   ```bash
   # Para Arch Linux
   sudo pacman -S --needed - < packageInstall/archLinux/pkglist.txt
   # Para paquetes del AUR (usando yay)
   yay -S --needed - < packageInstall/archLinux/aurlist.txt
   ```
3. Reinicia tu sesión de X11/Wayland y selecciona **Qtile** desde tu display manager.

## 📋 Dependencias Clave

| Dependencia | Rol |
| :--- | :--- |
| **Qtile** | Window Manager (Python base) |
| **Picom** | Compositor gráfico |
| **Alacritty** | Terminal acelerada por GPU |
| **Rofi** | Lanzador de aplicaciones y menús |
| **libinput-gestures** | Soporte de gestos para touchpad |
| **Flameshot** | Herramienta de capturas de pantalla |

## 🤝 Mantenimiento y Contribución

Este proyecto utiliza convenciones estrictas para mantener la claridad. Antes de realizar cambios, consulta el archivo `COMMIT_CONVENTIONS.md` para asegurar que el historial siga el formato estándar: `ADD(...)`, `UPDATE(...)` o `DELETE(...)`.

*   **Reportar errores:** Utiliza la sección de *Issues* del repositorio.
*   **Solicitudes de cambio:** Abre un *Pull Request* explicando los cambios realizados en los módulos correspondientes.

---
*Configuración mantenida bajo un flujo de trabajo modular y eficiente para entornos Linux avanzados.*