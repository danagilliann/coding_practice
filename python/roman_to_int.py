'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
I -> 1
II -> 2
V -> 5
X -> 10
L -> 50
C -> 100
D -> 500
M -> 1,000

I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1,000
'''

def roman_to_int(s):
        s = s.upper()
        result_int = 0
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        prev = 0
        current = 0

        for c in range(0,len(s)):
            if (c > 0):
                prev = s[c-1]
                # if the previous element is less than the current one
                if (roman_dict.get(prev) < roman_dict.get(s[c])): 
                    result_int -= roman_dict.get(prev)
                    result_int += (roman_dict.get(s[c]) - roman_dict.get(prev))
                else:
                    result_int += roman_dict.get(s[c])
            # the c is 0 so element will be added to the result immediately
            if (c == 0):
                result_int += roman_dict.get(s[c])

        return result_int

print roman_to_int("MCMXCVI")
