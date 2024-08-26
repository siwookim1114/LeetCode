from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = Counter(nums)
        for value in nums_map.values():
            if value > 1:
                return True
        return False