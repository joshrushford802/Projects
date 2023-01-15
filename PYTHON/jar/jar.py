class Jar:
    def __init__(self, capacity=12):
        if not capacity < 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if (not self.size + n > self.capacity) and (not n > self.capacity):
            self._size = self._size + n
        else:
            raise ValueError

    def withdraw(self, n):
        if not self.size < n:
            self._size = self._size - n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

jar = Jar()
print(jar)