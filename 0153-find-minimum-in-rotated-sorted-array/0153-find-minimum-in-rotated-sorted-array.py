class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_search(nums, l, r):
            print(l)
            print(r)
            print('...........')
            mid=(l+r)//2
            if nums[l]<=nums[r]:
                print('............')
                return nums[l]
                
            else:
                
                if nums[mid]<nums[l]:
                    r=mid
                    return binary_search(nums, l, r)
                else:
                    l=mid+1
                    return binary_search(nums,l,r)
        return binary_search(nums,0,len(nums)-1)
                
                
            
        