class Solution:
    def generateTag(self, c: str) -> str:
        # Split caption into words
        words = c.split()

        # Combine into camelCase with '#'
        tag = '#'
        for i, word in enumerate(words):
            cleaned = ''.join([ch for ch in word if ch.isalpha()])
            if cleaned == "":
                continue
            if i == 0:
                tag += cleaned.lower()
            else:
                tag += cleaned.capitalize()

        return tag[:100]
