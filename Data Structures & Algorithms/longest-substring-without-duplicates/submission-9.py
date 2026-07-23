class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        count=0
        mcount=0
        for i in range(0,len(s)):
            if s[i] in set1:
                set1.clear()
                count=1
                set1.add(s[i])
            else:
                set1.add(s[i])
                count+=1
                if count > mcount:
                    mcount = count
        return mcount
        