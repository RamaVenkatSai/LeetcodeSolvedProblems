class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            max_area=max(max_area,(r-l)*min(height[r],height[l]))
            if height[l]>height[r]:
                r-=1
            elif height[r]>=height[l]:
                l+=1
        return max_area
                