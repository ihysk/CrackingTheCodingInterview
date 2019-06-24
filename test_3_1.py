class FixedMultiStack:

    def __init__(self, size):
        self.number_of_stack = 3
        self.stack_capacity = size
        self.values = [] * self.number_of_stack * size
        self.sizes = [] * self.number_of_stack

    def push(self, index, val):
        if self.is_full(index):
            print(f'Stack {index} is full')
            return
        self.sizes[index] += 1
        self.values[self.index_of_top] = val

    def pop(self, index):
        if self.sizes[index] == 0:
            print(f'Stack {index} is empty')
            return
        val = self.values[self.index_of_top]
        self.values[self.index_of_top] = 0
        self.sizes[index] -= 1
        return val

    def peek(self, index):
        if self.sizes[index] == 0:
            print(f'Stack {index} is empty')
            return
        return self.values[self.index_of_top]

    def is_full(self, index):
        return self.sizes[index] == self.stack_capacity

    def index_of_top(self, index):
        return index * self.stack_capacity + self.sizes[index] - 1
