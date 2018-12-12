class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        pt = [0 for i in range(len(primes))]
        while n > 1:
            cur = [ugly[pt[i]] * primes[i] for i in range(len(primes))]
            umin = min(cur)
            for i in range(len(primes)):
                if umin == cur[i]: pt[i] += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
