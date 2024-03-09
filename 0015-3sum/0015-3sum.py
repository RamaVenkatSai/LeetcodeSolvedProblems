class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ll=[]
        if len(nums)==3 and nums[0]+nums[1]+nums[2]==0:
            return [nums]
        nums.sort()
        a=nums
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                if a[l]+a[r]+a[i]==0:
                    ll.append((a[i],a[l],a[r]))
                    l+=1
                    r-=1
                elif a[l]+a[r]+a[i]>0:
                    r=r-1
                elif a[l]+a[r]+a[i]<0:
                    l=l+1
        return set(ll)
        
                

