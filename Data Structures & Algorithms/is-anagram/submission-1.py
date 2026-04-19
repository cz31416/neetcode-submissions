class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for letter in s:
            if len(t) <= 0:
                return False
            else:
                t = t.replace(letter, "", 1)
        
        if len(t) > 0:
            return False
        
        return True