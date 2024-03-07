
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l=[0]*26
        for i in s:
            l[ord(i)-ord('a')]+=1
        for i in t:
            
            l[ord(i)-ord('a')]-=1
            if l[ord(i)-ord('a')]<0:
                return False
        if sum(l)==0:
            return True
        else:
            return False
            
        