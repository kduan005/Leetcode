class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        while n:
            if i == 0:
                if flowerbed[i] == 0:
                    if i+1 > len(flowerbed)-1 or flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    if i+1 > len(flowerbed)-1 or flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
            if i == len(flowerbed)-1:
                break
            i += 1
        return n == 0
        
