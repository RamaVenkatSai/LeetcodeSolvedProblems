class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_indexes={}
        maxer=0
        l=0
        for i in range(len(s)):
           
            if s[i] not in dict_indexes:
               dict_indexes[s[i]]=i
               maxer=max(maxer,i-l+1)
            elif s[i] in dict_indexes:
                
                if dict_indexes[s[i]]<l:
                    
                    maxer=max(maxer,i-l+1)
                    dict_indexes[s[i]]=i
                else:
                    
                    l=dict_indexes[s[i]]+1
                    dict_indexes[s[i]]=i
                    maxer=max(maxer,i-l+1)
                    
        return maxer

            
            
            