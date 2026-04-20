class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        big_dict = {}
        for word in strs:
            letter_count = len(word)
            product = 1
            for each in word:
                product = product * ord(each)
            data = (letter_count, product)
            if data not in big_dict:
                big_dict[data] = [word]
            else:
                big_dict[data].append(word)

        answer = []
        for word in big_dict:
            answer.append(big_dict[word])

        return answer