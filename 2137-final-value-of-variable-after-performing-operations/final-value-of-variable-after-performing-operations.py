class Solution:
    def finalValueAfterOperations(self, op: List[str]) -> int:
        a=op.count("X++")+op.count("++X")
        b=op.count("X--")+op.count("--X")
        return a-b