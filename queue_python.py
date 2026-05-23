class PythonQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = [None] * max_size
        self.head = 0
        self.tail = 0
        self.count = 0

    def push(self, value):
        if self.count >= self.max_size:
            return False
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.count += 1
        return True

    def pop(self):
        if self.count <= 0:
            return None
        value = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.count -= 1
        return value

    def clear(self):
        self.buffer = [None] * self.max_size
        self.head = 0
        self.tail = 0
        self.count = 0

    def find(self, value):
        for i in range(self.count):
            idx = (self.head + i) % self.max_size
            if self.buffer[idx] == value:
                return i
        return -1

    def is_empty(self):
        return self.count == 0