class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        j=0
        k=n-1
        max_cap=0
        while j < k:
            index=k-j
            if(heights[k]<=heights[j]):
                cap=heights[k]
                k-=1
            else:
                cap=heights[j]
                j+=1
            total_cap=index*cap
            if(total_cap > max_cap):
                max_cap=total_cap
            else:
                continue
        return max_cap
        