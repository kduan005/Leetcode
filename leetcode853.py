class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        p_s = sorted(zip(position, speed), reverse = True)
        count, t = 0, None
        for p, s in p_s:
            if not t or t * s + p < target:
                t = (float(target - p)) / s
                count += 1
        return count
