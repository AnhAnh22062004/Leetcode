class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_brackets = {"}" : "{", ")" : "(", "]" : "["}
        
        for char in s:
            if char in dict_brackets.values():
                stack.append(char)
            elif char in dict_brackets.keys():
                if not stack:
                    return False
                
                top_dict_brackets = stack[-1]
                if dict_brackets[char] ==  top_dict_brackets:
                    stack.pop()
                else: 
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True
    
solution = Solution()
s = "[{()}]"
result = solution.isValid(s)
print(result)
