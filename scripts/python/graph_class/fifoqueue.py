class fifoqueue:
    def __init__(self, length):
        self.data = [0] * length
        self.length = length
        self.head = 0
        self.tail = 0
        self.len = 0

    def enqueue(self, x):
        self.data[self.tail] = x
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail += 1
        self.len += 1


    def dequeue(self):
        x = self.data[self.head]
        if self.head == self.length:
            self.head = 0
        else:
            self.head += 1
        self.len -= 1
        return x

    def len(self):
        return self.len
