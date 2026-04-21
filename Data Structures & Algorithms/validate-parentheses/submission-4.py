class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        right = ('[', '(', '{')
        for each in s:
            if each in right:
                lst.append(each)
            elif len(lst) == 0:
                return False
            elif each == "]":
                if lst[-1] == "[":
                    lst.pop()
                else:
                    return False
            elif each == ")":
                if lst[-1] == "(":
                    lst.pop()
                else:
                    return False
            elif each == "}":
                if lst[-1] == "{":
                    lst.pop()
                else:
                    return False
        if len(lst) > 0:
            return False
        return True