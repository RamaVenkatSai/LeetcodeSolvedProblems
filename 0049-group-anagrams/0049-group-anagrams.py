class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def changer(i):
            l=[0]*26
            for j in i:
                l[ord(j)-ord('a')]+=1
            return tuple(l)
        ll=defaultdict(list)
        # print(ll)
        for i in strs:
            str1=changer(i)
            # print(str1)
            if str1 in ll:
                ll[str1].append(i)
            else:
                ll[str1]=[i]
        return list(ll.values())
            
            
        
        
        