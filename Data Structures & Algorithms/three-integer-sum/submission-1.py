class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        temp=set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    #if i!=j and i!=k and j!=k:
                    if nums[i]+nums[j]+nums[k] == 0:
                        triplet=tuple(sorted([nums[i],nums[j],nums[k]]))
                        temp.add(triplet)
        return list(temp)          