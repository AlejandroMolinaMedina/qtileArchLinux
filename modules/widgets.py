def init_widgets_list(widget, rotator):
    widgets_list = [
        widget.GroupBox(
            highlight_method="border",         
            borderwidth=2,                     
            this_current_screen_border="#FF5555", 
            this_screen_border="#FF5555",         
            other_current_screen_border="#A3BE8C", 
            other_screen_border="#A3BE8C",
            active="#ffffff",                     
            inactive="#4c566a",                   
        ),
        widget.Prompt(),
        widget.TaskList(
            icon_size=20,
            fmt='[{}]',
            font="sans",
            margin_y=3,
            padding_y=3,
            padding_x=5,
            highlight_method='border',
            border="#FFFFFF",
            borderwidth=0.5,
            rounded=True,
            title_width_method='uniform',
            max_title_width=40,
            parse_text=lambda text: "",
            theme_mode='preferred',
            theme_path='/usr/share/icons/Papirus',
        ),
        widget.Notify(
            foreground="#ffffff",
            background="#00000000",
            font="JetBrainsMono Nerd Font",
            fontsize=12,             
            padding=0,               
            margin_y=0,              
            line_height=1,           
            parse_text=lambda text: text.replace('\n', ' ').replace('\r', ''),
            scroll=True,
            scroll_step=3,
            scroll_interval=0.05,
            scroll_delay=2,
            width=200, 
            fmt='󰂚 {}', 
            action=True,
            default_timeout=5,
            name="notification_widget",
        ),
        widget.TextBox(text=' | ', foreground="#555555"),
        
        # Aquí solucionamos el problema del Lambda interno
        widget.GenPollText(
            func=lambda: "Iniciando...",
            update_interval=6,  
            name="volume_widget", 
            # IMPORTANTE: Activamos el marcado Pango para que respete los colores individuales <span foreground=...>
            markup=True, 
        ),
    ]
    
    # TRUCO: Inyectamos la referencia del widget exacto DESPUÉS de crear la lista
    # El índice [5] corresponde al ThreadPoolText dentro de la lista
    widgets_list[5].func = lambda w=widgets_list[5]: rotator.get_display_text(w)
    
    return widgets_list
