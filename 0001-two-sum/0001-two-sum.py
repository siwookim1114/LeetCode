class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for key, value in enumerate(nums):
            new = target - value
            if new in store:
                return [key, store[new]]
            store[value] = key