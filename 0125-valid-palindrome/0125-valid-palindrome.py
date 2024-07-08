## Initial Solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        s = s.lower()
        for char in s:
            if char.isalnum():
                arr.append(char)
        return arr[:] == arr[::-1]


## Second attempt solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # Regex Filtering
        s = re.sub('[^a-z0-9]', '', s)   ## replace characters that are NOT a-z or 0-9 with ''
        return s == s[::-1]  ## slicing
    

"""
Original algorithm was using list comprehension and use if statements to only receive characters that are alphanumerical. However, instead of using for loops and if statements, I 
thought of using regex to filter out non-alphanumericals using re.sub(). Worked out better. 
"""



        
