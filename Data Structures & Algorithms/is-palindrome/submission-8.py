class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for s1 in s:
            if s1.isalnum():
                newstr += s1.lower()
        i=0
        j=len(newstr) -1
        while i < j:
            if newstr[i] != newstr[j]:
                return False
            else:
                i+=1
                j-=1
        return True
        