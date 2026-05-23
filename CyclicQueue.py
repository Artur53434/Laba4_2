import ctypes

class CyclicQueue:
    def __init__(self, max_size=14):
        self.lib = ctypes.CDLL(r"D:\C_C++\Direct\Queue_lib_stl\x64\Debug\Queue_lib_stl.dll")

        # Настройка типов аргументов и возврата
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

        self.lib.isEmpty.argtypes = [ctypes.c_void_p]
        self.lib.isEmpty.restype = ctypes.c_bool

        # Создаём очередь
        self.queue_ptr = self.lib.create_queue(max_size)

    def __del__(self):
        if hasattr(self, 'queue_ptr') and self.queue_ptr:
            self.lib.delete_queue(self.queue_ptr)

    def push(self, value):
        return self.lib.push(self.queue_ptr, value)

    def pop(self):
        out = ctypes.c_int()
        success = self.lib.pop(self.queue_ptr, ctypes.byref(out))
        if success:
            return out.value
        else:
            return None  # или выбросить исключение

    def clear(self):
        self.lib.clear(self.queue_ptr)

    def find(self, value):
        return self.lib.find(self.queue_ptr, value)

    def is_empty(self):
        return self.lib.isEmpty(self.queue_ptr)
