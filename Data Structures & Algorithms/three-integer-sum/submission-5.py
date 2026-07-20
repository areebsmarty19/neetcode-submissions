class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        list1 = []
        nums = sorted(nums)
        i=0
        for i in range(0,len(nums)-1):
            left = i+1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0 and [nums[i],nums[left],nums[right]] not in list1:
                    list1.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1
                elif total > 0:
                    right -=1
                else:
                    left +=1
        return list1