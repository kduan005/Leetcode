class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [""]
        i = 0
        while i < len(s):
            if s[i] == "[":
                stack.append("")
            elif s[i] == "]":
                d = stack.pop()
                n = stack.pop()
                stack[-1] += n * d
            elif s[i].isdigit():
                j = i+1
                while j < len(s) and s[j].isdigit():
                    j += 1
                stack.append(int(s[i:j]))
                i = j-1
            else:
                stack[-1] += s[i]
            i += 1
        return stack[0]
                
