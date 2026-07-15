class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set()
        longest=1
        if len(nums) == 0:
            return 0
        for n in nums:
            s1.add(n)

        for n in nums:
            if n-1 not in s1:
                curr_len=1
                while n+1 in s1:
                    curr_len+=1
                    n+=1
                if n+1 in s1:
                    count+=1
                if curr_len > longest:
                    longest=curr_len
        return longest
                