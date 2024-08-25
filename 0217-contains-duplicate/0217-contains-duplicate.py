from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for value in Counter(nums).values():
            if value > 1:
                return True
        return False
        