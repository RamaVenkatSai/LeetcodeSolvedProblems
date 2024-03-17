class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        removed=0
        intervals=sorted(intervals,key=lambda x:x[0])
        res=[intervals[0]]
        for start,end in intervals[1:]:
            if start>=res[-1][1]:
                res.append([start,end])
                
            else:
                res[-1][1]=min(res[-1][1],end)
                removed+=1
        return removed
        