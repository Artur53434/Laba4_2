from ttkbootstrap import Style

def configure_styles():
    style = Style(theme='flatly')
    font = "Arial"
    
    style.configure("but.TButton",
                   font=(font, 9),
                   foreground="#000000",
                   background="#DBEAFE",
                   padding=(12, 5),
                   borderwidth=0,
                   width=22)
                    
    style.map("but.TButton",
             foreground=[('active', '#2D2D5C'), ('disabled', '#B8B8D8')],
             background=[('active', '#D0D0F0'), ('pressed', '#B0B0E0'), ('disabled', '#F8F8FF')])
    
    style.configure("Frame.TFrame",
                    background='white',
                    bordercolor="#DBEAFE",
                    borderwidth=1)
    return style