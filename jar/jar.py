def main():
    n = int(input('n: '))
    jar = Jar()
    jar.deposit(n)
    jar.withdraw(1)
    print(jar.size)
    print(jar.capacity)


class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0
        if int(capacity) <= 0 or not isinstance(capacity, int):
            raise ValueError('invalid capacity!')

    def __str__(self):
        return f"{int(self._size) * '🍪'}"

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError('no space for cookie!')
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("there's no enough cookies!")
        self._size -= n
        return n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



if __name__ == "__main__":
    main()