class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        operators = set(["+", "-", "*", "/"])
        for i in range(len(tokens)):
            value = tokens[i]
            if value in operators:
                y = int(numStack.pop())
                x = int(numStack.pop())
                if value == "+":
                    numStack.append((x + y))
                elif value == "-":
                    numStack.append((x - y))
                elif value == "*":
                    numStack.append((x * y))
                elif value == "/":
                    
                    numStack.append(int(x / y))
                
            else:
                numStack.append(value)
            #print(numStack)

        return int(numStack[-1])
                
        