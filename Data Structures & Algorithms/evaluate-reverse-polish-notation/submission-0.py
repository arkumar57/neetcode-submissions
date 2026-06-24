class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []

        for i in range(len(tokens)):

            if tokens[i] not in ('+', '-', '*', '/'):

                mystack.append(int(tokens[i]))

            
            if tokens[i] == '+':

                result = 0

                for k in range(2):

                    result += mystack.pop()

                mystack.append(result)


            if tokens[i] == '-':

                result = 0

                b = mystack.pop()
                a = mystack.pop()

                result = a - b
                    
                mystack.append(result)



            if tokens[i] == '*':

                result = 1

                for k in range(2):

                    result *= mystack.pop()
                    
                mystack.append(result)



            if tokens[i] == '/':

                b = mystack.pop()
                a = mystack.pop()



                result = int(a / b)

                mystack.append(result)
        

        return mystack.pop()