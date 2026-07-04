import subprocess
import shutil
from datetime import datetime
import re

class BarRotator:
    def __init__(self):
        # Mantenemos el estado de la rotación por pantalla
        self.screen_states = {}

    def get_display_text(self, qtile_widget):
        if not qtile_widget or not hasattr(qtile_widget, 'bar'):
            return "Cargando..."
            
        screen_idx = qtile_widget.bar.screen.index
        if screen_idx not in self.screen_states:
            self.screen_states[screen_idx] = 0
        
        current_shift = self.screen_states[screen_idx]
        
        # 1. Obtenemos los valores actuales de cada métrica (con sus colores usando formato Pango)
        # Usamos <span foreground='...'> para mantener tus colores originales en un solo string
        metrics = [
            f"<span foreground='#ffcc00'>{self.get_brightness()}</span>",  # 1
            f"<span foreground='#66ffff'>{self.get_volume()}</span>",      # 2
            f"<span foreground='#ffffff'>{self.get_clock()}</span>",       # 3
            f"<span foreground='#ffffff'>{self.get_battery()}</span>",      # 4
            f"<span foreground='#ffffff'>{self.get_cpu()}</span>",        # 5
            f"<span foreground='#ffffff'>{self.get_ram()}</span>",        # 6
            f"<span foreground='#ffffff'>{self.get_disk()}</span>"         # 7
        ]
        
        # 2. Aplicamos la rotación de la lista usando el "shift" actual
        # Si current_shift es 1, moverá el último elemento al principio, etc.
        rotated_metrics = metrics[-current_shift:] + metrics[:-current_shift]
        
        # 3. Unimos los elementos usando tu separador clásico con su color gris (#555555)
        separator = " <span foreground='#555555'>|</span> "
        full_text = separator.join(rotated_metrics)
        
        # 4. Incrementamos el shift para la siguiente vuelta (0 -> 1 -> 2 -> 3 -> 0...)
        self.screen_states[screen_idx] = (current_shift + 1) % len(metrics)
        
        return full_text

    def get_brightness(self):
        try:
            actual = int(open("/sys/class/backlight/intel_backlight/brightness").read())
            max_b = int(open("/sys/class/backlight/intel_backlight/max_brightness").read())
            percent = int((actual / max_b) * 100)
            return f"󰃟 {percent}%"
        except:
            return "󰃟 --%"

    def get_volume(self):
        try:
            res = subprocess.check_output(["pactl", "get-sink-volume", "@DEFAULT_SINK@"]).decode("utf-8")
            mute = subprocess.check_output(["pactl", "get-sink-mute", "@DEFAULT_SINK@"]).decode("utf-8")
            if "yes" in mute:
                return "󰝟 Muted"
            vol = re.search(r"(\d+)%", res).group(1)
            return f"󰕾 {vol}%"
        except:
            return "󰕾 --%"

    def get_clock(self):
        return datetime.now().strftime("%d-%m-%Y %a %H:%M:%S")

    def get_battery(self):
        try:
            capacity = open("/sys/class/power_supply/BAT0/capacity").read().strip()
            status = open("/sys/class/power_supply/BAT0/status").read().strip()
            
            if status == "Charging":
                char = "⚡" # Cargando
            elif status in ["Not charging", "Unknown"]:
                char = "🔌" # Conectado a la corriente, batería en bypass por TLP
            else:
                char = "🔋" # Usando batería (Discharging)
                
            return f"{char} {capacity}%"
        except:
            return "🔋󰁹 --%"

    def get_cpu(self):
        try:
            # Obtiene el uso de CPU promedio basado en top
            cpu_usage = subprocess.check_output("top -bn1 | grep 'Cpu(s)' | awk '{print $2 + $4}'", shell=True).decode("utf-8").strip()
            return f" {cpu_usage}%"
        except:
            return " --%"

    def get_ram(self):
        try:
            # Calcula el uso de RAM leyendo /proc/meminfo
            mem = dict((i.split()[0].rstrip(':'), int(i.split()[1])) for i in open('/proc/meminfo').readlines())
            used = mem['MemTotal'] - mem['MemAvailable']
            percent = int((used / mem['MemTotal']) * 100)
            return f" {percent}%"
        except:
            return " --%"

    def get_disk(self):
        try:
            # Calcula el uso de almacenamiento raíz
            total, used, free = shutil.disk_usage("/")
            percent = int((used / total) * 100)
            return f"󰋊 {percent}%"
        except:
            return "󰋊 --%"
