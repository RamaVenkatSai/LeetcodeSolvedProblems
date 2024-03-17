class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals=sorted(intervals, key =lambda x:x[0])
        res=[]
        res.append(intervals[0])
        for start, end in intervals[1:]:
            if start> res[-1][1]:
                res.append([start,end])
            else:
                res[-1][0]=min(start,res[-1][0])
                res[-1][1]=max(end,res[-1][1])
            
        return res
    