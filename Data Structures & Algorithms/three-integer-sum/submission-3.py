class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        temp=set()
        nums=sorted(nums)
        i=0
        target=0
        j=i+1
        k=n-1
        for i in range(0,n):
            j=i+1
            k=n-1
            while(j<k):
                target = nums[i]+nums[j]+nums[k]
                if target < 0:
                    j+=1
                elif target > 0:
                    k-=1
                elif target == 0:
                    triplet=tuple([nums[i],nums[j],nums[k]])
                    temp.add(triplet)
                    j+=1
                    k-=1
                else:
                    continue
        return list(temp)          