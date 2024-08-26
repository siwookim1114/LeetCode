class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            center = (left + right) // 2
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            else:
                right = center - 1
        
        left, right = 0, len(nums) - 1
        if nums[left] < target < nums[right]:
            while left <= right:
                center = (left + right) // 2
                if nums[center] < target:
                    left = center + 1
                else:
                    right = center -1
                    
            return left 
        
        elif target > nums[right]:
            return right + 1
        else:
            return left
            
        