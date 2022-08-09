class Stack:
    def __init__(self, task):
        self.task = task
        self.stack = []

    def is_empty(self):
        if not self.stack:
            return True

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
