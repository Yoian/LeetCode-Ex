class Solution():
    def isPalindrome(self, x):
        x = str(x)    
        if x == x[::-1]:
            return True
        else: return False
    
Hola=Solution()
print(Hola.isPalindrome(121))