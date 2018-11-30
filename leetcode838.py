class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        stack = [[],[]]
        i, last = 0, None
        while i <= len(dominoes):
            if i == len(dominoes):
                last = stack.pop()
            elif dominoes[i] == 'R':
                last = stack.pop()
                stack.append(['R'])
            elif dominoes[i] == 'L':
                stack[-1].append('L')
                last = stack.pop()
                stack.append([])
            else:
                stack[-1].append(dominoes[i])
            i += 1
            if last:
                if 'L' in last and 'R' in last:
                    mid = len(last)/2
                    if len(last) % 2 == 1:
                        for j in range(mid+1, len(last)):
                            last[j] = 'L'
                    else:
                        for j in range(mid, len(last)):
                            last[j] = 'L'
                    for j in range(mid):
                        last[j] = 'R'
                elif 'R' in last:
                    for j in range(len(last)):
                        last[j] = 'R'
                elif 'L' in last:
                    for j in range(len(last)):
                        last[j] = 'L'
                stack[0] += last
                last = None
        return ''.join(stack[0])
        
