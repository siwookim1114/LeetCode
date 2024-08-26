class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        for item in jewels:
            jewels_set.add(item)
        
        cnt = 0
        for ele in stones:
            if ele in jewels:
                cnt +=1
        
        return cnt
            
        
        
        
        