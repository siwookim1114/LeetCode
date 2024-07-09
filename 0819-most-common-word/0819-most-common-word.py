class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z0-9]', ' ', paragraph)
        new = paragraph.split(' ')
        counts = collections.defaultdict(int)
        for char in new:
            if char not in banned and char.isalnum():
                counts[char] += 1
        return max(counts, key = counts.get)


"""
Summary Analysis: Was able to extract the paragraph into substrings by applying regex filtering and splitting by spaces. However, I first wasn't able to proceed more after dividing the words into pieces. 
1. Tried to use dictionary method but got stuck in retrieving the key with the max value. I figured out that using collections.defaultdict(int), I am able to apply counts[char(subwords)] += 1 in iteration, and then
return the max value by max(counts, key = counts.get method).

defaultdict(int) : dictionary
When printing counts: defaultdict(<class 'int'>, {'bob': 1, 'a': 1, 'ball': 2, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
=> max(counts, key = counts.get) : Output = key which has the max value
dictionary get() method : Returns the value of the item with the specified key

"""

