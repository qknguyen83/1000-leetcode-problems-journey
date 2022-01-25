class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0]) < 97:
            if word[1:] == word[1:].upper() or word[1:] == word[1:].lower():
                return True
        else:
            if word[1:] == word[1:].lower():
                return True
        return False
