class Solution:
    def isValid(self, s: str) -> bool:
        #create a map first 
        # for loop
        #make sure you have teh stack is not empty and the close has a match
        #if it's open append it
        #return trur if there is no stack and False if there is a stack

        stack=[]
        matching={']':'[',
             '}':'{',
             ')':'('}
        for c in s:
            if c in matching:
                if stack and matching[c]==stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack)==0

                
        