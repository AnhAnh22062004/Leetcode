class Solution:
    def romanToInt(self, s: str) -> int:
        dict_roman_number = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0 
        count = 0
        while(count < len(s)):
            if count + 1 < len(s) and dict_roman_number[s[count]] < dict_roman_number[s[count + 1]]:
                total += dict_roman_number[s[count + 1]] - dict_roman_number[s[count]]
                count = count + 2 
            else:
                total = total + dict_roman_number[s[count]]
                count = count + 1
                
        return total 
        
s = str(input())
result = Solution().romanToInt(s)
print(result)
