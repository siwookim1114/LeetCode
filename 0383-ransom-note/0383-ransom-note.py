class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rndict = defaultdict(int)
        mzdict = defaultdict(int)
        for string in ransomNote:
            rndict[string] +=1
        for string in magazine:
            mzdict[string] += 1
    
        for key, value in rndict.items():
            if mzdict[key] < value:
                return False
        return True
            