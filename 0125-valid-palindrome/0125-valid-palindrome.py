class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for char in s:
            if char.isalnum():
                arr.append(char)
        if arr[:] == arr[::-1]:
            return True
        
    



        