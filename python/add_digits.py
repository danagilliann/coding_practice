num = 6345
my_int = 0

def add_total(num):
        total = 0
        string_of_num = str(num)

        for i in range(0, len(string_of_num)):
                total += int(string_of_num[i])
        return total

total = add_total(num)

def add_digits(num, total):
        if total <= 10:
                print total
        else:
                num = total
                total = add_total(num)
                add_digits(num, total)

add_digits(num, total)
