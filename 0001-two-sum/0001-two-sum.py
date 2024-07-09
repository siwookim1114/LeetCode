class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for key, value in enumerate(nums):
            new = target - value
            if new in store:
                return [key, store[new]]
            store[value] = key

"""
Analysis: Instead of using brute force which has a O(n^2) time complexity, by using a dictionary hash table, it could reduce the time complexity to O(1) or O(n) in the worst case. Hence by declaring a dictionary
and storing the key, value inside the dictionary by {value:index}, I could declare a new target by target - value, and search inside the dictionary for the corresponding value right away. If not inside, add it on to the
dictionary. 

Resulted in very high time complexity. 
"""
