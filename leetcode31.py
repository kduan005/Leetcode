class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i >= 1 and nums[i] <= nums[i-1]:
            i -= 1
        i -= 1
        if i >= 0:
            for j in reversed(range(i+1, len(nums))):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
