# Ожидается, что скомпилированный модуль называется queue_cpp_pybind.pyd (или .so)
try:
    import queue_cpp_pybind as cpp_lib
except ImportError:
    raise ImportError("Не найден скомпилированный модуль queue_cpp_pybind. Скомпилируйте C++ код через pybind11!")

class CppQueue:
    def __init__(self, max_size):
        self.queue = cpp_lib.CppQueue(max_size)

    def push(self, value):
        return self.queue.push(value)

    def pop(self):
        if self.queue.is_empty():
            return None
        return self.queue.pop()

    def clear(self):
        self.queue.clear()

    def find(self, value):
        return self.queue.find(value)

    def is_empty(self):
        return self.queue.is_empty()