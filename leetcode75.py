class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for k in range(len(nums)):
            if nums[k] == 0:
                nums[k], nums[j] = nums[j], nums[k]
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[k] == 1:
                nums[k], nums[j] = nums[j], nums[k]
                j += 1
