class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            else:
                if (i - first[char] - 1) != distance[ord(char) - ord('a')]:
                    return False
        return True
