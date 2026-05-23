import tkinter
from tkinter import ttk, messagebox
from ttkbootstrap import Style
from VisualQueue import VisualQueue
import button_logic  
from styles import configure_styles

class MainForm:
    def __init__(self):
        self.style = configure_styles()
        self.root = self.style.master
        self.root.title("GUI для работы с циклической очередью")
        self.root.geometry("750x550")
        self.root.resizable(width=False, height=False)
        
        self._create_menu()
        self._create_frames()
        
        self.visual_queue = VisualQueue(self.canvas_visual, backend_type=3)
        self._create_widgets()

        self.root.mainloop()

    def _create_menu(self):
        menubar = tkinter.Menu(self.root)
        self.root.config(bg="#EFF6FF", menu=menubar) 
        file_menu = tkinter.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Программа", menu=file_menu)
        file_menu.add_command(label="Справка", command=lambda: messagebox.showinfo("Справка", "..."))
        file_menu.add_command(label="Выход", command=self.root.destroy)

    def _create_frames(self):
        self.frame_visual = ttk.Frame(self.root, relief="solid", style="Frame.TFrame", width=500, height=500)
        self.frame_visual.grid(row=0, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        self.canvas_visual = tkinter.Canvas(self.frame_visual, bg="white", width=400, height=400)
        self.canvas_visual.pack(padx=10, pady=10, expand=True)

        self.frame_setting = ttk.Frame(self.root, relief="solid", style="Frame.TFrame")
        self.frame_setting.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.frame_operations = ttk.Frame(self.root, relief="solid", style="Frame.TFrame")
        self.frame_operations.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        self.frame_select_lang = ttk.Frame(self.root, relief="solid", style="Frame.TFrame")
        self.frame_select_lang.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

    def _create_widgets(self):
        # --- Настройка очереди ---
        ttk.Label(self.frame_setting, text="Настройка очереди", width=25).grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ttk.Separator(self.frame_setting, orient="horizontal").grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        ttk.Label(self.frame_setting, text="Задать размер очереди:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_size = ttk.Entry(self.frame_setting, width=5)
        self.entry_size.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        
        ttk.Button(self.frame_setting, text="+ Создать", style="but.TButton",
                   command=lambda: button_logic.create(self.visual_queue, self.entry_size)).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        # --- Операции ---
        ttk.Label(self.frame_operations, text="Операции").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ttk.Separator(self.frame_operations, orient="horizontal").grid(row=1, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        ttk.Label(self.frame_operations, text="Значение:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.entry_value = ttk.Entry(self.frame_operations, foreground="Gray")
        self.entry_value.insert(0, "Значение")
        self.entry_value.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.entry_value.bind("<FocusIn>", lambda e: self._clear_placeholder(e, self.entry_value, "Значение"))
        self.entry_value.bind("<FocusOut>", lambda e: self._set_placeholder(e, self.entry_value, "Значение"))

        ttk.Button(self.frame_operations, text="Добавить", style="but.TButton",
                   command=lambda: button_logic.add(self.visual_queue, self.entry_value)).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
        
        ttk.Button(self.frame_operations, text="Взять один элемент", style="but.TButton",
                   command=lambda: button_logic.get(self.visual_queue)).grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        ttk.Separator(self.frame_operations, orient="horizontal").grid(row=5, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        
        ttk.Label(self.frame_operations, text="Поиск:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.entry_find = ttk.Entry(self.frame_operations, foreground="Gray")
        self.entry_find.insert(0, "Поиск...")
        self.entry_find.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        self.entry_find.bind("<FocusIn>", lambda e: self._clear_placeholder(e, self.entry_find, "Поиск..."))
        self.entry_find.bind("<FocusOut>", lambda e: self._set_placeholder(e, self.entry_find, "Поиск..."))
        
        ttk.Button(self.frame_operations, text="Найти", style="but.TButton",
                   command=lambda: button_logic.find(self.visual_queue, self.entry_find)).grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

        ttk.Button(self.frame_operations, text="Очистить все элементы", style="but.TButton",
                   command=lambda: button_logic.delete(self.visual_queue)).grid(row=8, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # --- Выбор языка ---
        ttk.Label(self.frame_select_lang, text="Реализация:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.lang_var = tkinter.IntVar(value=3) # По умолчанию Python (чтобы работало из коробки)
        
        ttk.Radiobutton(self.frame_select_lang, text="C (ctypes)", variable=self.lang_var, 
                        value=1, command=self._on_lang_change).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(self.frame_select_lang, text="C++ STL (pybind)", variable=self.lang_var, 
                        value=2, command=self._on_lang_change).grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(self.frame_select_lang, text="Python", variable=self.lang_var, 
                        value=3, command=self._on_lang_change).grid(row=2, column=0, padx=5, pady=5, sticky="w")

    def _on_lang_change(self):
        new_lang = self.lang_var.get()
        if self.visual_queue.count == 0:
            self.visual_queue.backend_type = new_lang
            if self.visual_queue.max_size > 0:
                self.visual_queue.init_backend(self.visual_queue.max_size)
            return

        res = messagebox.askyesnocancel(
            "Смена реализации", 
            "В очереди есть элементы. Что с ними сделать?\n\n"
            "Да - Перенести в новую реализацию\n"
            "Нет - Очистить очередь и переключиться\n"
            "Отмена - Остаться на текущей реализации"
        )

        if res is True: # Перенос
            items = self.visual_queue.get_all_items()
            self.visual_queue.backend_type = new_lang
            self.visual_queue.init_backend(self.visual_queue.max_size)
            for item in items:
                self.visual_queue.push(item)
        elif res is False: # Очистка
            self.visual_queue.backend_type = new_lang
            self.visual_queue.init_backend(self.visual_queue.max_size)
            self.visual_queue.draw()
        else: # Отмена
            self.lang_var.set(self.visual_queue.backend_type)

    def _clear_placeholder(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, tkinter.END)
            entry.config(foreground="black")

    def _set_placeholder(self, event, entry, text):
        if entry.get() == '':
            entry.insert(0, text)
            entry.config(foreground="gray")