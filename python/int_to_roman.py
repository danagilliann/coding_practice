def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        str_n = str(num)
        curr = 0
        holder = 0
        int_el = 0
        val = 0
        
        roman_d = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        
        for i in range(0, len(str_n)):
            int_el = int(str_n[i])
            
            if (int_el != 0):
                if (len(str_n) == 1):
                    curr = (int_el * (10 ** (len(str_n)-1)))
                else:
                    curr = (int_el * (10 ** (len(str_n)-1-i)))
                
                if (int_el != 5):
                    curr /= int_el
                
                if (int_el == 5):
                    roman += (roman_d[curr])
                
                if (int_el == 4):
                    val = curr * (1 + int_el)
                    roman += (roman_d[curr] + roman_d[curr*5])
                if (int_el == 9):
                    val = curr * 10
                    roman += (roman_d[curr] + roman_d[val])
                if (int_el > 5) and (int_el < 9):
                    roman += (roman_d[curr * 5] + roman_d[curr]*(int_el-5))
                if (int_el <= 3):
                    roman += roman_d[curr] * int_el
                
        return roman

print intToRoman(4)
