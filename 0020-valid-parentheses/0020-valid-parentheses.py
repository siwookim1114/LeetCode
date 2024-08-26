from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stk = deque()
        paran_dict = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for ele in s:
            if ele not in paran_dict:
                stk.append(ele)
            else:
                if stk and paran_dict[ele] == stk[-1]:
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        else:
            return True
