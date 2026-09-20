class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))

        else:
            last_el = self.stack[-1]
            if val > last_el[-1]:
                self.stack.append((val, last_el[-1]))
            else:
                 self.stack.append((val,val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        last_el = self.stack[-1]
        return last_el[-1]
        