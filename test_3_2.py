class StackWithMin(list):

    def __init__(self):
        self.vals = []
        self.min_list = []

    def push(self, val):
        self.vals.append(val)
        if len(self.min_list) == 0:
            self.min_list.append(val)
        elif self.min_list[-1] > val:
            self.min_list.append(val)

    def pop(self):
        if len(self.vals) == 0:
            print(f'Stack doesn\' have any value')
            return
        val = self.vals.pop()
        if self.min_list[-1] == val:
            self.min_list.pop()
        return val

    def min(self):
        if len(self.min_list) == 0:
            print(f'Stack doesn\'t have any value')
        return self.min_list[-1]
