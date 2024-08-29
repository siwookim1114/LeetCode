class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(min):
                min = nums[i]
            elif nums[i] > min and abs(nums[i]) == abs(min):
                min = nums[i]
        return min