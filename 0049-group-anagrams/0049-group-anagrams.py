class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """


        # Firstly here there are two things to remember
        # Dictionary cannot have keys as mutable values such as list or another dictionary it can take only immutable datatypes i.e; tuple or string
        # Here just we got the individualk count of 26 alphabets and joined them according to count of respective alphabets and printed the values
        ll=collections.defaultdict(list)
        
        for i in strs:
            counter=[0]*26
            for m in i:

                counter[ord(m)-ord('a')]=counter[ord(m)-ord('a')]+1
            ll[str(counter)].append(str(i))
        return ll.values()
