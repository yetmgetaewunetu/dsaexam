
class Stack_using_list:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)
    def pop(self):
        if len(self.stack) <= 0:
            print("empty stack!")
            return
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def getSize(self):
        return len(self.stack)
    def display(self):
        print(*self.stack)

my = Stack_using_list()
my.pop()
my.push(2)
my.push(3)
my.push(4)
my.push(5)
my.push(6)
my.push(7)
my.pop()
my.display()
