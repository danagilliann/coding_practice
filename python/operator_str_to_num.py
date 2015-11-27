
def string_to_number(string):
    temp_num = ""
    operators = ["*", "+", "-", "/"]
    chars = string.split()
    op = ""
    
    add = 0
    minus = 0
    multi = 0
    div = 0
    
    a = 0
    mi = 0
    mu = 0
    d = 0
    
    num = 0
    
    count = 0
    
    error = "invalid"
    
    #print chars
    # take account spaces
    if len(chars) % 2 == 0:
        return error
    
    for c in chars:
        
        if count % 2 == 0:
            if c in operators:
                return error
        else:
            if c not in operators:
                return error
        
        if count == 0:
            c = int(c) #coerce c
            num = c
            
        if c in operators:
            op = c

        else: 
            c = int(c) # coerce c
            if op == "+":
                a += num
                num += c 
            elif op == "-":
                mi += num 
                num -= c
            elif op == "*":
                num = ((num-(mi+a))*c)+(mi+a)
            elif op == "/":
                num = ((num-(mi+a))/c)+(mi+a)
        
        count += 1
        print count

            
    return num

print string_to_number("1 + 2 +")
        
    
# 
# Your previous Plain Text content is preserved below:
# 
# Write a function/method that takes a mathematical expression represented as a string and returns the value of the expression.
# 
# The expression is written in infix notation (number operator number) with a single space between operators and operands.
# 
# You only need to support four operations: addition, subtraction, division and multiplication (+ - * /)
# 
# No parenthesis.
# 
# Valid input:
# "15 + 2 - 3" -> 14
# "145" -> 145
# "1 + 233 / 233" -> 2
# 
# 
# 
# Invalid input:
# "1 1"
# "+ 1"
# "1 + 2 +"
# "+ 1 1"
# "1+2"
# 
# 
# 





