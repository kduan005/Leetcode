class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[-1]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                else:
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1
        return res

                
