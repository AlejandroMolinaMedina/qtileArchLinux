# Qtile Arch Linux Modular Configuration

![Qtile](https://img.shields.io/badge/Qtile-Latest-blue)
![Arch Linux](https://img.shields.io/badge/OS-Arch%20Linux-blueviolet)
![License](https://img.shields.io/badge/License-MIT-green)

Una configuración de **Qtile** altamente personalizada, modular y moderna diseñada específicamente para **Arch Linux**. Este entorno está optimizado para ofrecer un flujo de trabajo eficiente, una estética minimalista y un mantenimiento sencillo mediante una estructura de archivos desacoplada.

## 🚀 Características Principales

*   **BarRotator**: Gestión inteligente de la barra de estado mediante una rotación cíclica de métricas (brillo, volumen, reloj, batería) para maximizar el espacio disponible.
*   **Gestión Dinámica de Grupos**: Mapeo automático de aplicaciones basado en `WM_CLASS`, con soporte para creación/eliminación en tiempo real y reordenamiento numérico.
*   **Estética Moderna**: Configuración curada de `Picom` (efectos de desenfoque y transparencias) y `Alacritty` para una experiencia visual cohesiva.
*   **Gestos Táctiles**: Integración avanzada con `libinput-gestures` para un control gestual intuitivo en dispositivos portátiles.
*   **Modularidad**: Lógica separada por responsabilidades, facilitando la personalización de widgets, funciones auxiliares y reglas de usuario sin comprometer el archivo principal.

## 📂 Estructura del Proyecto

```text
├── alacritty/               # Configuración del terminal
├── modules/                 # Lógica de widgets, funciones y autostart
├── packageInstall/          # Listas de paquetes para Arch (pacman/AUR) y Fedora
├── picom/                   # Configuración del compositor (blur/shadows)
├── styles/                  # Estilos visuales de la barra (Pango/CSS)
├── utils/                   # Gestión dinámica de grupos y reglas
├── config.py                # Punto de entrada principal y atajos de teclado
└── gestures/                # Configuración de libinput-gestures
```

## 🛠️ Instalación Rápida

### 1. Requisitos Previos
Asegúrate de tener un entorno gráfico base. Instala las dependencias necesarias utilizando los scripts proporcionados según tu distribución:

*   **Arch Linux:** 
    ```bash
    sudo pacman -S --needed - < packageInstall/archLinux/pkglist.txt
    # Opcional: Instalar paquetes AUR
    yay -S --needed - < packageInstall/archLinux/aurlist.txt
    ```
*   **Fedora:**
    ```bash
    sudo dnf install $(cat packageInstall/fedora/pkglist.txt)
    ```

### 2. Configuración
Copia este repositorio en tu carpeta de configuración local:
```bash
git clone <url-del-repositorio> ~/.config/qtile
```

### 3. Ejecución
Reinicia tu sesión de X11/Wayland y selecciona `Qtile` en tu gestor de inicio de sesión (Display Manager).

## 📋 Dependencias Clave

| Dependencia | Rol |
| :--- | :--- |
| **Qtile** | Window Manager (Python-based) |
| **Picom** | Compositor (transparencias y efectos) |
| **Alacritty** | Emulador de terminal acelerado por GPU |
| **Rofi** | Lanzador de aplicaciones y menús |
| **libinput-gestures** | Soporte de gestos para touchpad |
| **Flameshot** | Herramienta de capturas de pantalla |

## 🤝 Contribuciones y Estándares

El proyecto sigue un estándar estricto para mantener la calidad del historial de cambios. Antes de realizar cualquier contribución, consulta:

*   **[COMMIT_CONVENTIONS.md](COMMIT_CONVENTIONS.md)**: Guía obligatoria para el formato de mensajes de commit (`ADD`, `UPDATE`, `DELETE`).
*   **[GEMINI.md](GEMINI.md)**: Notas técnicas adicionales sobre el desarrollo.

## 📝 Soporte
Si encuentras un error o tienes una propuesta de mejora, abre un **Issue** en el repositorio. Para discusiones rápidas o dudas sobre la configuración, revisa la documentación oficial de [Qtile](https://docs.qtile.org/).

---
*Configuración mantenida bajo estándares de modularidad y eficiencia para entornos Linux.*