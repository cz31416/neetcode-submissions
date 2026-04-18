class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.cap == self.size:
            self.resize()

        for i in range(self.cap):
            if self.arr[i] == n:
                self.arr[i] = 0
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        ret = self.arr[self.size - 1]
        self.arr[self.size - 1] = 0
        self.size -= 1
        return ret

    def resize(self) -> None:
        newcap = self.cap * 2
        newarr = [0] * newcap
        for i in range(self.size):
            newarr[i] = self.arr[i]
        self.arr = newarr
        self.cap = newcap

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap