class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict1={}
        l=0
        maxer=0
        max_len=0
        for index,i in enumerate(s):
            dict1[i]=1+dict1.get(i,0)
            maxer=max(maxer,dict1[i])
            
            if maxer+k < (index-l+1):
            
                dict1[s[l]]-=1
                l+=1
            max_len=max(max_len,index-l+1)
                
        return max_len


        