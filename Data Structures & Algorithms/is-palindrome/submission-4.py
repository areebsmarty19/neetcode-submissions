class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        n=len(s)
        for i in range(0,n):
            if s[i] == s[(n-1)-i]:
                flag=1
            else:
                return False
        return True
        