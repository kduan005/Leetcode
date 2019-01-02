class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack, i = [], 0
        while i < len(path):
            if path[i] != "/":
                j = i+1
                while j < len(path) and path[j] != "/":
                    j += 1
                s = path[i:j]
                if s == ".":
                    i += 1
                elif s == "..":
                    if stack:
                        stack.pop()
                    i += 2
                else:
                    stack.append(s)
                    i = j
            else:
                i += 1
        return "/" + "/".join(stack)
