class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        l=0
        dict1={}
        max_len=0
        len1=0
        for r in range(len(s)):
            if s[r] in dict1 and dict1[s[r]]<l:
                max_len=max(max_len,r-l+1)
                dict1[s[r]]=r
            elif s[r] in dict1 and dict1[s[r]]>=l:
                l=dict1[s[r]]+1
                max_len=max(max_len,r-l+1)
                dict1[s[r]]=r    
            else:
                dict1[s[r]]=r
                max_len=max(max_len,r-l+1)
        return max_len
            
            
            