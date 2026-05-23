from dataclasses import dataclass
from math import cos, sin, pi
from tkinter import messagebox

@dataclass
class Point:
    x: float
    y: float

class Circle:
    def __init__(self, circle_id, text_id, coor):
        self.circle_id = circle_id
        self.text_id = text_id
        self.coor = coor

class VisualQueue:
    def __init__(self, canvas, backend_type=3):
        self.canvas = canvas
        self.max_size = 0
        self.w = 400
        self.h = 400
        self.R = 140  # Радиус окружности
        self.r = 28   # Радиус ячеек
        self.circles = []
        
        # Внутреннее состояние визуализации (для точной отрисовки кольца)
        self.items = []
        self.head = 0
        self.count = 0
        
        self.backend_type = backend_type
        self.backend = None

    def init_backend(self, max_size):
        self.max_size = max_size
        self.items = [None] * max_size
        self.head = 0
        self.count = 0
        
        if self.backend_type == 1:
            from queue_c import CQueue
            self.backend = CQueue(max_size)
        elif self.backend_type == 2:
            from queue_cpp_pybind import CppQueue
            self.backend = CppQueue(max_size)
        else:
            from queue_python import PythonQueue
            self.backend = PythonQueue(max_size)

    def draw(self):
        self.canvas.delete("all")
        if self.max_size <= 0: return

        self.w = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 400
        self.h = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 400

        # Рисуем каркас
        cx, cy = self.w / 2, self.h / 2
        self.canvas.create_oval(cx - self.R, cy - self.R, cx + self.R, cy + self.R, outline="gray", width=2, dash=(4, 2))
        
        self.circles = []
        step = 2 * pi / self.max_size
        
        # Рисуем ячейки
        for i in range(self.max_size):
            angle = -pi/2 + step * i  # Начинаем с верха
            x = cx + self.R * cos(angle)
            y = cy + self.R * sin(angle)
            
            c_id = self.canvas.create_oval(x - self.r, y - self.r, x + self.r, y + self.r, fill="#F0F8FF", outline="gray", width=2)
            t_id = self.canvas.create_text(x, y, text="", font=("Arial", 10, "bold"))
            self.circles.append(Circle(c_id, t_id, Point(x, y)))
            
            # Заполняем значения
            if self.items[i] is not None:
                self.canvas.itemconfig(t_id, text=str(self.items[i]))
                self.canvas.itemconfig(c_id, fill="#DBEAFE")

        # Рисуем указатели Начала и Конца
        if self.count > 0:
            tail_idx = (self.head + self.count) % self.max_size
            
            h_circle = self.circles[self.head]
            self.canvas.create_text(h_circle.coor.x, h_circle.coor.y + self.r + 15, 
                                    text="Начало (Head)", fill="red", font=("Arial", 8, "bold"))
            self.canvas.itemconfig(h_circle.circle_id, outline="red", width=3)

            if self.count < self.max_size: # Если очередь не полная, рисуем Хвост
                t_circle = self.circles[tail_idx]
                self.canvas.create_text(t_circle.coor.x, t_circle.coor.y - self.r - 15, 
                                        text="Конец (Tail)", fill="blue", font=("Arial", 8, "bold"))
                self.canvas.itemconfig(t_circle.circle_id, outline="blue", width=3)
            else: # Если полная, Хвост совпадает с Головой
                self.canvas.create_text(h_circle.coor.x, h_circle.coor.y - self.r - 15, 
                                        text="Очередь полна", fill="purple", font=("Arial", 8, "bold"))

    def push(self, value):
        if self.count >= self.max_size:
            return False
        tail_idx = (self.head + self.count) % self.max_size
        self.items[tail_idx] = value
        self.count += 1
        self.backend.push(value)
        self.draw()
        return True

    def pop(self):
        if self.count <= 0:
            return None
        val = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.count -= 1
        self.backend.pop()
        self.draw()
        return val

    def find(self, value):
        # Ищем через бэкенд для честности, но визуально подсвечиваем
        pos = self.backend.find(value)
        if pos != -1:
            idx = (self.head + pos) % self.max_size
            self.canvas.itemconfig(self.circles[idx].circle_id, fill="#90EE90") # Зеленый цвет найденного
            messagebox.showinfo("Успех", f"Элемент найден на логической позиции {pos + 1}")
            # Вернем цвет через время или при следующем действии (здесь просто перерисовываем)
        else:
            messagebox.showinfo("Системное сообщение", "Данное значение не найдено в очереди")
        self.draw()

    def clear(self):
        self.items = [None] * self.max_size
        self.head = 0
        self.count = 0
        if self.backend:
            self.backend.clear()
        self.draw()

    def get_all_items(self):
        """Возвращает список элементов в логическом порядке"""
        res = []
        for i in range(self.count):
            res.append(self.items[(self.head + i) % self.max_size])
        return res