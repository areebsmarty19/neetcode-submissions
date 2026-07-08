class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(char for char in s if char.isalnum()).lower()
        revs =s1[::-1]
        print(revs)
        if revs == s1:
            return True
        else:
            return False
        