class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = defaultdict(int)
        for num in nums:
            nums_dict[num] += 1
        for value in nums_dict.values():
            if value > 1:
                return True
        return False