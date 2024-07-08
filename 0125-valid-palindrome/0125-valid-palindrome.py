class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # Regex Filtering
        s = re.sub('[^a-z0-9]', '', s)   ## replace characters that are NOT a-z or 0-9 with ''
        return s == s[::-1]  ## slicing
    



        