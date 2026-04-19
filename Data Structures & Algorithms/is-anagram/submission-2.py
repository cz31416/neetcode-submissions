class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        
        for letter in t:
            if letter not in count:
                return False
                        
            count[letter] -= 1
            if count[letter] < 0:
                return False

        for each in count:
            if count[each] > 0:
                return False

        return True