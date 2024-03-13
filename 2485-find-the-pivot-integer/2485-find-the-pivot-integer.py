class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        total=(n*(n+1))//2
        for i in range(1,n):
            
            l=(i*(i+1))//2
            if (2*l==total+i):
                return i
        return -1