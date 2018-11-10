class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sw = [float('-inf') for i in range(3)]
        for num in nums:
            if num > sw[0]:
                sw[0], sw[1], sw[2] = num, sw[0], sw[1]
            elif sw[0] > num > sw[1]:
                sw[1], sw[2] = num, sw[1]
            elif sw[1] > num > sw[2]:
                sw[2] = num
        return sw[2] if sw[2] != float('-inf') else sw[0]
                
