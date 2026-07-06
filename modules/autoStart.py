import os
import subprocess
from libqtile.log_utils import logger

class autostart:
    @staticmethod
    def startAppps():
        home = os.path.expanduser('~')
        logger.info("Iniciando procesos de autostart...")

        # Abrir un archivo de log para capturar salidas de las apps
        log_file = open(os.path.expanduser('~/.local/share/qtile/apps.log'), 'a')

        apps = [
            ["libinput-gestures-setup", "start"],
            ["autorandr", "--change"],
            ['xss-lock', '--', 'transfer-sleep-lock', '--', 'i3lock', '-c', '000000'],
            ['xbindkeys']
        ]

        for app in apps:
            try:
                # Redirigimos la salida al log file para poder debugear
                subprocess.Popen(app, stdout=log_file, stderr=log_file)
                logger.info(f"Proceso lanzado: {' '.join(app)}")
            except Exception as e:
                logger.error(f"Error al ejecutar {' '.join(app)}: {e}")

        # Comandos complejos con shell=True
        shell_cmds = [
            f"picom --config {home}/.config/picom/picom.conf",
            f"bash {home}/.secrets/scripts/wallpaper_daemon.sh",
            "brightnessctl set 15%"
        ]

        for cmd in shell_cmds:
            try:
                subprocess.Popen(cmd, shell=True, stdout=log_file, stderr=log_file)
                logger.info(f"Comando lanzado: {cmd}")
            except Exception as e:
                logger.error(f"Error al ejecutar {cmd}: {e}")