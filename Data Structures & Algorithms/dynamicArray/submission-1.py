class DynamicArray:


    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n
        return


    def pushback(self, n: int) -> None:
        if self.capacity == self.size:
            self.resize()
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        pop = self.array[self.size - 1]
        self.size -= 1
        return pop
 

    def resize(self) -> None:
        temp_array = self.array 
        self.capacity = self.capacity * 2
        self.array = [None] * self.capacity
        for idx, val in enumerate(temp_array):
            self.array[idx] = val



    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity