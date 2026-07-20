class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        sum = 0
        while i <= j:
            width = j - i
            height = min(heights[j],heights[i])
            total = width * height

            if total > sum :
                sum = total
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return sum
        