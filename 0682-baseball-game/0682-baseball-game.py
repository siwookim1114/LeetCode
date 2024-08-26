from collections import deque
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = deque()
        for operation in operations:
            if operation == "+":
                stk.append(stk[-1] + stk[-2])
            elif operation == "D":
                stk.append(2 * stk[-1])
            elif operation == "C":
                stk.pop()
            else:
                stk.append(int(operation))
        return sum(stk)
        

        