from libqtile.log_utils import logger

def add_new_group_manually(qtile):
    """
    Crea manualmente un nuevo grupo con etiqueta de círculo, hasta un máximo de 9.
    """
    if len(qtile.groups) >= 9:
        logger.warning("Máximo de 9 grupos alcanzado.")
        return

    new_name = str(len(qtile.groups) + 1)
    qtile.add_group(new_name, label="●")
    logger.warning(f"Grupo {new_name} creado.")

def delete_current_group(qtile):
    """
    Elimina el grupo actual, reordena los grupos restantes numéricamente
    y protege el grupo '1'.
    """
    current_group = qtile.current_group
    if current_group.name == "1":
        logger.warning("No se puede eliminar el grupo principal.")
        return
    if len(qtile.groups) <= 1:
        logger.warning("No se puede eliminar el último grupo.")
        return
    
    # 1. Cambiar al grupo '1' antes de eliminar el actual
    qtile.groups_map["1"].toscreen()
    
    # 2. Eliminar el grupo
    qtile.delete_group(current_group.name)
    
    # 3. Reordenar los grupos restantes
    # Convertimos a enteros para ordenar correctamente
    groups = sorted([g for g in qtile.groups if g.name.isdigit()], key=lambda g: int(g.name))
    
    new_groups_map = {}
    for i, group in enumerate(groups, start=1):
        new_name = str(i)
        if group.name != new_name:
            # Renombrar grupo
            group.name = new_name
        new_groups_map[new_name] = group
    
    qtile.groups_map = new_groups_map
            
    logger.warning("Grupo eliminado y grupos reordenados.")

def get_available_group(qtile, max_windows=3):
    """
    Busca un grupo con menos de N ventanas. Si todos están llenos, intenta crear uno nuevo hasta el límite de 9.
    """
    for group in qtile.groups:
        if len(group.windows) < max_windows:
            return group.name
    
    # Si todos están llenos, intentar crear uno nuevo si no hemos llegado a 9
    if len(qtile.groups) < 9:
        new_name = str(len(qtile.groups) + 1)
        qtile.add_group(new_name, label="●")
        return new_name
    
    # Si llegamos al límite, devolvemos el último grupo disponible
    return qtile.groups[-1].name

def go_to_group(qtile, name):
    """
    Cambia al grupo si existe.
    """
    if name in qtile.groups_map:
        qtile.groups_map[name].toscreen()
    else:
        logger.error(f"Grupo {name} no encontrado")

def move_window_to_group(qtile, name):
    """
    Mueve la ventana al grupo si existe.
    """
    if name in qtile.groups_map:
        qtile.current_window.togroup(name, switch_group=True)
    else:
        logger.error(f"Grupo {name} no encontrado")
