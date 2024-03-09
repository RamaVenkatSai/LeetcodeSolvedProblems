class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                stack.append(i)
            elif(i==')' or i=='}' or i==']'):   
                if(i=='}'):
                    if(stack==[] or stack[-1]!='{'):
                        return False
                    
                elif( i==']'):
                    if(stack==[] or stack[-1]!='['):
                        return False
                    
                elif( i==')'):
                    if(stack==[] or stack[-1]!='('):
                        return False
                stack.pop()
        if(stack==[]):
            return True
      
            