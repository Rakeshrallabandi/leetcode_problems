class MyQueue:

    def __init__(self):
        
        self.n=[]
    def push(self, x: int) -> None:
        self.n.append(x)

    def pop(self) -> int:
        return self.n.pop(0)

    def peek(self) -> int:
        return self.n[0]

    def empty(self) -> bool:
        return  True if len(self.n)==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()