
'''    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pass '''
class Solution(object):
    def isValid(s: str) -> bool:
    # Dictionary to hold matching pairs
    # bracket_map = {')': '(', ']': '[', '}': '{'}
    # stack = []
    
    # Loop through each character in the string
    for char in s:
        # If it's a closing bracket
        if char in bracket_map:
            # Pop from stack if not empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # It's an opening bracket, push it to the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched
    return not stack

# Example usage:
print(isValid("()"))      # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False







    



  

