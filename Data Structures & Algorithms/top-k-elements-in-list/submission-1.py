class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output={}
        result=[]
        for nums1 in nums:
            output[nums1]= nums.count(nums1)
        sorted_dic=sorted(output.items(),key=lambda item: item[1],reverse=True)
        for i in range(k):
            number = sorted_dic[i][0]
            result.append(number)
        return result
