class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        
        while l <= r:
            
            mid = (l + r)//2 #FYI: Right bit shift by 1 is equivalent to dividing by 2 and is more efficient.
            
            #If the subarr size is 1 or the sub arr isn't rotated then we instantly know the min value.
            if nums[l] <= nums[r]:
                return nums[l]
            #If the array is rotated, then we must find the inflection point in the rotated half
            else:
                #If the left half is rotated take it but include the middle b/c the min value could be mid itself
                if nums[mid] < nums[l]:
                    r = mid
                #Take the right half, the inflection point cannot include mid
                else:
                    l = mid+1
            