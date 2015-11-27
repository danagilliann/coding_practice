def excel_sheet(c): 
        c = c.lower()
        a_ascii = ord("a")
        z_ascii = ord("z")

        if len(c) == 1:
                return (ord(c) - a_ascii + 1)
        else:
            return ((z_ascii - a_ascii + 1) * (len(c) - 1)) + (ord(c[len(c)-1]) - a_ascii + 1)

print excel_sheet("BBA")
