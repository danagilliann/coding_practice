'''

Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
   A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

'''

def excel_sheet(s): 
        s = s.lower()
        a_ascii = ord('a')
        z_ascii = ord('z')
        ret = 0
        char = ""

        if len(s) == 1:
                return (ord(s) - a_ascii + 1)
        else:
                for c in range(0, len(s)):
                        char = s[c]
                        ret += ((26 ** (len(s) - c - 1)) * (ord(char) - a_ascii + 1))
                return ret
