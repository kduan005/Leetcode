class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for op in tokens:
            if op not in "+-*/":
                stack.append(int(op))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if op == "+":
                    stack.append(op1 + op2)
                elif op == "-":
                    stack.append(op1 - op2)
                elif op == "*":
                    stack.append(op1 * op2)
                else:
                    stack.append(int(op1 * 1.0 / op2))
        return stack[0]
