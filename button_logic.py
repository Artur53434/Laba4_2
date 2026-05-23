from tkinter import messagebox
from VisualQueue import VisualQueue

def create(vqueue: VisualQueue, entry_size):
    try:
        max_size = int(entry_size.get())
        if max_size <= 0 or max_size > 14: 
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число от 1 до 14.")
        return
    
    vqueue.init_backend(max_size)
    vqueue.draw()

def add(vqueue: VisualQueue, entry_value):
    text = entry_value.get()
    if text == "Значение" or text == "":
        messagebox.showerror("Ошибка", "Введите значение.")
        return
    try:
        value = int(text)
        if abs(value) > 99999: raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число в интервале [-99999; 99999].")
        return
    
    if not vqueue.push(value):
        messagebox.showinfo("Внимание", "Очередь полная.")

def get(vqueue: VisualQueue):
    if vqueue.count == 0:
        messagebox.showinfo("Внимание", "Очередь пуста.")
        return
    val = vqueue.pop()
    messagebox.showinfo("Извлечено", f"Из очереди извлечен элемент: {val}")

def find(vqueue: VisualQueue, entry_find):
    text = entry_find.get()
    if text == "Поиск..." or text == "":
        messagebox.showerror("Ошибка", "Введите значение для поиска.")
        return
    try:
        value = int(text)
        if abs(value) > 99999: raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите целое число в интервале [-99999; 99999].")
        return
    vqueue.find(value)

def delete(vqueue: VisualQueue):
    vqueue.max_size = 0
    vqueue.items = []
    vqueue.count = 0
    vqueue.head = 0
    vqueue.backend = None
    vqueue.draw()