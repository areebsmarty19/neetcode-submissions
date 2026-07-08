class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         if (len(s)!=len(t)):
            return False
         i=0
         j=0
         s = sorted(s)
         t = sorted(t)
         while i<len(s) and j<len(t):
            if (s[i]!=t[j]):
               return False
            i+=1
            j+=1
         return True



