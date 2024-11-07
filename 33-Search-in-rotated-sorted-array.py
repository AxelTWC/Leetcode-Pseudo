class Solution:
    def search(self, nums: List[int], target: int) -> int:
    #     lstSize = len(nums) - 1
    #     start = 0
    #     if len(nums) == 1 or len(nums) == 0:
    #         return -1
    #     while (start < lstSize):
    #         mid = (lstSize + start) // 2


    #         if nums[] target < nums[mid-1]: # if target is smaller than the middle number
    #             lstSize = index(nums[mid-1]) # Size is 3 for example 1 
    #             if nums[mid] == target: # If target meets 
    #                 return mid
    #             elif start != lstSize:
    #                 start = start + 1
    #             elif start == lstSize:
    #                 return -1
    #             else:
    #                 return -1

    #         elif target > nums[mid+1]:
    #             lstSize = index(nums[mid])
    #             if nums[mid] == target:
    #                 return mid
    #             elif start != lstSize:
    #                 start = start + 1
    #             elif start == lstSize:
    #                 return -1
    #             else: 
    #                 return -1    
    #         else:
    #             return -1
    #     return -1
    
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

        