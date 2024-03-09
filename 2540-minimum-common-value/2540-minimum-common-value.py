class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[0]==nums2[0]:
            return nums2[0]
        
        ptr1, ptr2=0,0
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1]==nums2[ptr2]:
                return nums1[ptr1]
            elif nums1[ptr1]<nums2[ptr2]:
                ptr1+=1
            elif nums1[ptr1]>nums2[ptr2]:
                ptr2+=1
        return -1
        
    
                
                    
        