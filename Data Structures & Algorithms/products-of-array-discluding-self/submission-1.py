class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list1=[]
        i=0
        while i <len(nums):
            j=0
            temp=1
            while j<len(nums):
                if i == j:
                    j+=1
                    continue
                else:
                    temp = temp*nums[j]
                    j+=1
            list1.append(temp)
            i+=1
        return list1


        
        