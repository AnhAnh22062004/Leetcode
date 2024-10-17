class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        reserved = 0 
        original = x
        x_str = str(x) 
        count = len(x_str)  
        while count > 0:
            reserved = reserved * 10 + int(x_str[count - 1])
            count = count - 1
            
        return x == reserved


x = int(input())
result = Solution().isPalindrome(x)
print(result)
