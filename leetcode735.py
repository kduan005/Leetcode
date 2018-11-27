class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for ast in asteroids:
            if ast < 0:
                while stack and 0 < stack[-1] < abs(ast):
                    stack.pop()
                if stack and stack[-1] + ast == 0:
                    stack.pop()
                    continue
                if stack and stack[-1] > abs(ast):
                    continue
                else:
                    stack.append(ast)
            else:
                stack.append(ast)
        return stack
