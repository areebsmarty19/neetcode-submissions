class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            exit
        nums1=set(nums)
        num1=[]
        count1=1
        print(nums1)
        n=len(nums1)
        for num in nums1:
            if num-1 in nums1:
                continue
            else:
                while num+1 in nums1:
                    count1+=1
                    num=num+1
                num1.append(count1)
                count1=1
        count=max(num1)
        return count    