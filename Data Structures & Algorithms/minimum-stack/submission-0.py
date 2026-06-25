class MinStack:

    def __init__(self):

        self.mystack = []
        

    def push(self, val: int) -> None:

        self.mystack.append(val)
        

    def pop(self) -> None:

        del self.mystack[-1]
        

    def top(self) -> int:

        return self.mystack[-1]
        

    def getMin(self) -> int:

        return min(self.mystack)
        
