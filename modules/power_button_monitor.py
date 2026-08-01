import evdev
import subprocess
import threading
from libqtile.log_utils import logger

# Ruta del dispositivo del botón de encendido (verificado previamente)
DEVICE_PATH = "/dev/input/event11"
POWERMENU_SCRIPT = "/home/al3xmm14/.config/rofi/applets/bin/powermenu.sh"

def monitor_power_button():
    try:
        device = evdev.InputDevice(DEVICE_PATH)
        logger.warning(f"Iniciando monitor de botón en {DEVICE_PATH}")
        for event in device.read_loop():
            # Log de todos los eventos para depuración
            if event.type == evdev.ecodes.EV_KEY:
                logger.warning(f"Evento recibido: type={event.type}, code={event.code}, value={event.value}")
            
            # El evento de pulsación suele ser EV_KEY, tipo 1, código 116 (KEY_POWER)
            if event.type == evdev.ecodes.EV_KEY and event.code == evdev.ecodes.KEY_POWER and event.value == 1:
                logger.warning("Botón de encendido detectado, lanzando powermenu")
                subprocess.Popen([POWERMENU_SCRIPT])
    except Exception as e:
        logger.error(f"Error en monitor_power_button: {e}")

def start_power_button_monitor():
    thread = threading.Thread(target=monitor_power_button, daemon=True)
    thread.start()
    logger.warning("Monitor de botón de encendido iniciado en segundo plano")
