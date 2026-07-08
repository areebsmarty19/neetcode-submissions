class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        og=set()
        n=len(s)
        l=0
        res=0
        for r in range(0,n):
            while s[r] in og:
                og.discard(s[l])
                l+=1
            og.add(s[r])
            if res<r-l+1:
                res=r-l+1
        return res
