class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ll=[]
        for i,a in enumerate(nums):
            
            if i>0 and a==nums[i-1] :
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                
                if nums[i]+nums[l]+nums[r]>0:
                    r=r-1
                elif nums[i]+nums[l]+nums[r]<0:
                    l=l+1
                else :
                    ll.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                

        return ll
                