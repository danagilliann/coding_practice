binary = 0
count = 0

def decimal_to_bin(n):
    global binary
    global count

    # base case
    if n == 0:
        print binary
    else:
        binary += (n % 2) * 10 ** count
        count += 1
        decimal_to_bin(n/2)

decimal_to_bin(27)

