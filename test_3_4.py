class MyQueue:

    def __init__(self):
        self.stack_new = []
        self.stack_old = []

    def size(self):
        return len(self.stack_new) + len(self.stack_old)

    def add(self, val):
        self.stack_new.append(val)

    def shift_stack(self):
        while self.stack_new != []:
            self.stack_old.append(self.stack_new.pop())

    def peek(self):
        self.shift_stack()
        self.stack_old[-1]

    def remove(self):
        self.shift_stack()
        return self.stack_old.pop()
