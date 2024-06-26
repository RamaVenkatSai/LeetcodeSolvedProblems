class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda k:k[0])
        output=[intervals[0]]
        for start,end in intervals[1:]:
            prevend=output[-1][1]
            if start<= prevend:
                output[-1][1]=max(prevend,end)
            else:
                output.append([start,end])
        return output
        
        