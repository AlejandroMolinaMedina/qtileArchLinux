# Qtile Arch Linux Modular Configuration

Una configuración de **Qtile** altamente personalizada, modularizada y moderna diseñada para **Arch Linux**. Este entorno está pensado para ser eficiente, estéticamente agradable y fácil de mantener.

## 🚀 Características Principales

*   **BarRotator (Barra inteligente)**: Optimiza el espacio de la barra de estado mediante una rotación cíclica de métricas (brillo, volumen, reloj, batería).
*   **Gestión Dinámica de Grupos**: Mapeo automático de aplicaciones a escritorios virtuales basado en `WM_CLASS` y capacidad de crear/eliminar grupos en tiempo real con reordenamiento numérico automático.
*   **Estética Moderna**: Configuración curada de *Picom* (sombras, bordes redondeados, transparencias) y *Alacritty*.
*   **Gestos Táctiles**: Integración fluida con `libinput-gestures`.
*   **Mantenimiento Sencillo**: Estructura modular que separa la lógica de las funciones, los estilos y las reglas de los grupos.

## 📂 Estructura del Proyecto

```text
├── config.py                 # Punto de entrada y atajos de teclado
├── modules/                  # Lógica de widgets y funciones auxiliares
├── styles/                   # Estilos Pango/CSS de la barra
├── utils/                    # Definición de grupos y reglas de aplicaciones
├── packageInstall/           # Listas automatizadas de paquetes (Arch/Fedora)
└── .scripts/                 # Herramientas de automatización
```

## 🛠️ Instalación Rápida

Este repositorio incluye scripts y listas de paquetes para una configuración rápida. Consulta los archivos en `packageInstall/` para instalar las dependencias necesarias.

### 📋 Dependencias del Sistema
Para que la configuración funcione correctamente, asegúrate de tener instalados los siguientes componentes:

| Dependencia | Descripción | Documentación |
| :--- | :--- | :--- |
| **[Qtile](https://qtile.org/)** | Gestor de ventanas principal | [Docs](https://docs.qtile.org/) |
| **[Picom](https://github.com/yshui/picom)** | Compositor (sombras, blur) | [Wiki](https://github.com/yshui/picom/wiki) |
| **[Alacritty](https://alacritty.org/)** | Emulador de terminal | [Docs](https://alacritty.org/config-alacritty.html) |
| **[Rofi](https://github.com/davatorium/rofi)** | Lanzador de aplicaciones | [Wiki](https://github.com/davatorium/rofi/wiki) |
| **[libinput-gestures](https://github.com/bulletmark/libinput-gestures)** | Gestos de touchpad | [Repo](https://github.com/bulletmark/libinput-gestures) |
| **[Flameshot](https://flameshot.org/)** | Capturas de pantalla | [Docs](https://flameshot.org/docs/) |
| **[brightnessctl](https://github.com/Hummer12007/brightnessctl)** | Control de brillo | [Repo](https://github.com/Hummer12007/brightnessctl) |
| **[Nerd Fonts](https://www.nerdfonts.com/)** | Iconos (JetBrainsMono, Symbols) | [Web](https://www.nerdfonts.com/) |

Adicionalmente, instala los paquetes listados en `packageInstall/` usando tu gestor de paquetes (`pacman`/`yay` en Arch Linux).

## 🤝 Contribuciones y Estándares

Para mantener el historial de commits ordenado, por favor sigue nuestras **[Convenciones de Commit](COMMIT_CONVENTIONS.md)**.
*   Cada cambio debe ser un commit individual siguiendo el formato: `ADD(...)`, `UPDATE(...)` o `DELETE(...)`.

---
*Configuración inspirada en un flujo de trabajo modular y eficiente para entornos Linux.*
