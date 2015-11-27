# Enter your code here. Read input from STDIN. Print output to STDOUT
no_of_test_cases = int(raw_input())
numbers = []
v = 0
x = 6

for t in range(1, no_of_test_cases+1):
    numbers.append(int(raw_input()))

for N in numbers:
    x = 6
    if (N%5 == 0) and (N-5 != 0): 
        print(N*'5')
    else: # N%5 != 0
        if N-5 == 0:
            print(N*'3')
        elif N-3 == 0:
            print(N*'5')
        else:
            while (x % 5 != 0) and (x > 5):
                v += 3
                x = N-v 
                       
            if x%5 == 0:
                print(("5"*v) + ("3"*x))
            
            # logic below must be fixed
            if (x < 5) and (x % 5 != 0):
                if N%3 == 0:
                    print("5"*N)
                elif N%3 != 0:
                    print(-1)
            
          
