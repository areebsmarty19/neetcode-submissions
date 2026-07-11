class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        i=0
        diff=0
        for num in nums:
            diff=target-num
            if diff in dict1 :
                return [dict1[diff],i]
            else:
                dict1[num]=i
                temp=num
                i+=1
        return [dict1[diff],dict1[temp]]