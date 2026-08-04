import evdev
import subprocess
import threading
import os
from libqtile.log_utils import logger

# Ruta del script del menú de energía
POWERMENU_SCRIPT = "/home/al3xmm14/.config/rofi/applets/bin/powermenu.sh"

def find_power_button_device():
    """Busca el dispositivo 'Intel HID 5 button array' dinámicamente."""
    for path in evdev.list_devices():
        try:
            device = evdev.InputDevice(path)
            if device.name == "Intel HID 5 button array":
                return device
        except Exception:
            continue
    return None

def monitor_power_button():
    device = find_power_button_device()
    if not device:
        logger.error("No se pudo encontrar el dispositivo 'Intel HID 5 button array'")
        return

    try:
        logger.warning(f"Iniciando monitor de botón en {device.path} ({device.name})")
        for event in device.read_loop():
            # Intentar detectar el evento de pulsación (value=1)
            if event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_POWER and event.value == 1:
                logger.warning("Botón de encendido detectado, ejecutando powermenu...")
                
                # Crear un entorno donde hostname es uname -n
                env = os.environ.copy()
                env["PATH"] = "/usr/bin:/bin:/usr/sbin:/sbin:" + env.get("PATH", "")
                
                # Ejecutar el script
                subprocess.Popen(POWERMENU_SCRIPT, shell=True, env=env, executable='/bin/bash')

    except Exception as e:
        logger.error(f"Error en monitor_power_button: {e}")

def start_power_button_monitor():
    thread = threading.Thread(target=monitor_power_button, daemon=True)
    thread.start()
    logger.warning("Monitor de botón de encendido iniciado en segundo plano")
