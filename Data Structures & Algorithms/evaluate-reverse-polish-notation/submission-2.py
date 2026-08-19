import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+" : operator.add,
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : lambda a, b: int(a / b)
        }
        stack = []
        for tok in tokens :
            if tok not in operands :
                stack.append(int(tok))
            else :
                left = stack.pop()
                right = stack.pop()
                result = operands[tok](right,left)
                stack.append(result)
        return stack.pop()