class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def sortMedian(nums, left, right):
            rand = random.randint(left, right)
            pi = nums[rand]
            nums[rand], nums[right] = nums[right], nums[rand]
            i = j = left
            for k in range(left, right):
                if nums[k] < pi:
                    nums[k], nums[j] = nums[j], nums[k]
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[k] == pi:
                    nums[k], nums[j] = nums[j], nums[k]
                    j += 1
            nums[right], nums[j] = nums[j], nums[right]
            if i <= mid <= j:
                return
            elif mid > j:
                sortMedian(nums, j+1, right)
            else:
                sortMedian(nums, left, i-1)

        left, right = 0, len(nums)-1
        mid, half = len(nums)/2, (len(nums)+1)/2
        sortMedian(nums, left, right)
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]        
