import os

def macropadKeys(Key, mod, lazy):
    # Definición de scripts disponibles
    SCRIPTS = {
        "1": {"hash": "2abf35d8ac52fc717715b970e207d4f4065c2c358a248a06f1f6cf23389099fa", "name": "login"},
        "2": {"hash": "8a823c207792ef228e377638d5f7505370cb437e8d7f61fc0260abbd9b6a6e8c", "name": "session-pre.sh"},
        "3": {"hash": "0034fb9c7065b7ce2957cb7f522f542c858adf7cbaff709d3a3fe7cd1588554d", "name": "session-qa.sh"},
        "4": {"hash": "640b0d5793a32a061b050bfd878bb156314511d070bed9746cad320c31a6e5fe", "name": "start-instance-qa.sh"},
    }

    home_dir = os.path.expanduser("~/.secrets/hashScripts")
    
    # Ejecuta el script de bash directamente dentro de una terminal Alacritty.
    keys_list = [
        Key([mod], "1", lazy.spawn(f"alacritty -e bash {os.path.join(home_dir, SCRIPTS["1"]["hash"])}")),
        Key([mod], "2", lazy.spawn(f"alacritty -e bash {os.path.join(home_dir, SCRIPTS["2"]["hash"])}")),
        Key([mod], "3", lazy.spawn(f"alacritty -e bash {os.path.join(home_dir, SCRIPTS["3"]["hash"])}")),
        Key([mod], "4", lazy.spawn(f"alacritty -e bash {os.path.join(home_dir, SCRIPTS["4"]["hash"])}")),
    ]
    return keys_list

