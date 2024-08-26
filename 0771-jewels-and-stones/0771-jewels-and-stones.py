class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        stones_set = defaultdict(int)
        for item in jewels:
            jewels_set.add(item)
        for stone in stones:
            stones_set[stone] +=1
            
        cnt = 0
        for key in stones_set.keys():
            if key in jewels_set:
                cnt += stones_set[key]
        
        return cnt
                