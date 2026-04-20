import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c not in string.punctuation)
        chars = list(s.lower().replace(" ", ""))
        for i in range(round(len(chars)/2)):
            if chars[i] != chars[len(chars) - 1 - i]:
                return False
        return True