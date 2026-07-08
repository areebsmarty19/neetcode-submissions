class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums1=list(set(nums))
        num1=[]
        count1=1
        nums1.sort()
        print(nums1)
        n=len(nums1)
        for i in range(0,n-1):
            if(nums1[i]+1==nums1[i+1]):
                count1+=1
            else:
                num1.append(count1)
                count1=1
        num1.append(count1)
        count=max(num1)
        return(count)    