class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        mcount = 0
        i = 0
        j = 0
        
        while j < len(s):
            while s[j] in set1:
                set1.remove(s[i])
                i += 1
            set1.add(s[j])
            count = j - i + 1
            if count > mcount:
                mcount = count

            j += 1
            
        return mcount