class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(char for char in s if char.isalnum()).lower()
        n=len(s1)
        for i in range(0,n):
            if s1[i] == s1[(n-1)-i]:
                flag=1
            else:
                return False
        return True
        