import ctypes
import os

class CQueue:
    def __init__(self, max_size):
        # ќжидаем, что dll лежит р€дом с main файлом
        dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "queue_c.dll")
        self.lib = ctypes.CDLL(dll_path)

        self.lib.create_queue.argtypes = [ctypes.c_int]
        self.lib.create_queue.restype = ctypes.c_void_p

        self.lib.delete_queue.argtypes = [ctypes.c_void_p]
        self.lib.delete_queue.restype = None

        self.lib.push.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.push.restype = ctypes.c_bool

        self.lib.pop.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int)]
        self.lib.pop.restype = ctypes.c_bool

        self.lib.clear.argtypes = [ctypes.c_void_p]
        self.lib.clear.restype = None

        self.lib.find.argtypes = [ctypes.c_void_p, ctypes.c_int]
        self.lib.find.restype = ctypes.c_int

        self.lib.is_empty.argtypes = [ctypes.c_void_p]
        self.lib.is_empty.restype = ctypes.c_bool

        self.queue_ptr = self.lib.create_queue(max_size)

    def __del__(self):
        if hasattr(self, 'queue_ptr') and self.queue_ptr:
            self.lib.delete_queue(self.queue_ptr)

    def push(self, value):
        return self.lib.push(self.queue_ptr, value)

    def pop(self):
        out = ctypes.c_int()
        if self.lib.pop(self.queue_ptr, ctypes.byref(out)):
            return out.value
        return None

    def clear(self):
        self.lib.clear(self.queue_ptr)

    def find(self, value):
        return self.lib.find(self.queue_ptr, value)

    def is_empty(self):
        return self.lib.is_empty(self.queue_ptr)