class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashchar = {")" : "(", "]" : "[", "}" : "{" }

        for i in s:
            if i in hashchar:
                if stk and stk[-1] == hashchar[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)
        
        return  True if not stk else False
