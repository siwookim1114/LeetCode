from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        if count_s == count_t:
            return True
        else:
            return False

    # def isAnagram(self, s: str, t: str) -> bool:
    #     s, t = sorted(s), sorted(t)
    #     s_string, t_string = "".join(s), "".join(t)
    #     if s_string == t_string:
    #         return True
    #     else:
    #         return False

