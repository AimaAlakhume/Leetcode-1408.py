class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []

        allWords = ' '.join(words)

        for word in words:
            if allWords.count(word) > 1:
                output.append(word)

        return output
