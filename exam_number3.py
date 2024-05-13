class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, data):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(data)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def peek(self):
        return self.stack1[-1]
    def dequeue(self):
        if not self.stack1:
            print("the stack is empty,nothing to remove!")
            return -1
        return self.stack1.pop()

    def display(self):
        print(*self.stack1)

my = Queue()
# my.dequeue()
my.enqueue(1)
my.display()
my.enqueue(2)
my.display()
my.enqueue(3)
my.display()
my.enqueue(4)
my.enqueue(5)
my.enqueue(6)
print(my.dequeue())
print(my.dequeue())
print(my.dequeue())
print(my.peek())
