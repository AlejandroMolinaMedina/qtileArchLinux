#!/bin/bash
# Ruta del LED
LED_PATH="/sys/class/leds/platform::micmute/brightness"

# Verificamos el estado actual del control 'Capture'
# 'amixer sget Capture' devuelve [on] o [off]
STATUS=$(/usr/bin/amixer sget Capture | grep -o "\[on\]")

if [ -n "$STATUS" ]; then
    # Si está en [on], lo silenciamos (nocap) y encendemos el LED (1)
    /usr/bin/amixer sset Capture nocap
    echo 1 | /usr/bin/tee $LED_PATH > /dev/null
else
    # Si está en [off], lo activamos (cap) y apagamos el LED (0)
    /usr/bin/amixer sset Capture cap
    echo 0 | /usr/bin/tee $LED_PATH > /dev/null
fi
