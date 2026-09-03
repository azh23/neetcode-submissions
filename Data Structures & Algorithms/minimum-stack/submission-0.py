class MinStack:

    def __init__(self):
        self.st = []
        self.minimums = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minimums:
            self.minimums.append(min(self.minimums[-1], val))
        else:
            self.minimums.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minimums[-1]
        
