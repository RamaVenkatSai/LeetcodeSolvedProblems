class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        removed=0
        intervals=sorted(intervals,key=lambda x:x[0])
        res=[intervals[0]]
        for i in intervals[1:]:
            if res[-1][1]<=i[0]:
                res.append(i)
            else:
                removed+=1
                res[-1][1]=min(i[1],res[-1][1])
        return removed
        