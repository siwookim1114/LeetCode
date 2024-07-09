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

