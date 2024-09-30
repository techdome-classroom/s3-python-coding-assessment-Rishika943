class Solution(object):
   ''' def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        pass
'''

class Solution(object):
    def romanToInt(s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
        # If the current value is smaller than the next value, subtract it
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            # Otherwise, add the current value to the total
            total += roman_map[s[i]]
    
    return total

# Example usage:
print(romanToInt("III"))      # Output: 3
print(romanToInt("LVIII"))    # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 199
  
    
    
  

