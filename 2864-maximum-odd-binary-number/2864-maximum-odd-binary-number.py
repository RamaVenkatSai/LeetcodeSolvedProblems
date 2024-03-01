class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter=0
        for i in s:
            
            if i=="1":
                counter=counter+1
        n=len(s)
        
        l=[]
        print(counter)
        for i in range(n-1):
            if i<counter-1:
                l.append("1")
            else:
                l.append("0")
        l.append("1")
        print(l)
        return "".join(l)
                
            
            
        