'''class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass'''
        
class Solution:
    def isValid(s: str) -> bool:
        bracket_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
             if char in bracket_map:
            
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it to the stack
            stack.append(char)
            return not stack

# Example usage:
print(isValid("()"))      # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))
    

    
          # Output: False







    



  

