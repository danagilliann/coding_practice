def is_prime(n):
	boolean = True
	for r in range(2, n):
		if n % r == 0:
			boolean = False
			break
	return boolean

def find_primes(n):
	p_list = []
	boolean = True
	for r in range(2, n):
		boolean = is_prime(r)
		if boolean == True:
			p_list.append(r)
	
	return p_list

def prime_less_million(n):
	p_list = find_primes(n)
	num = 0
	index = 0
	for i in range(0, len(p_list)-1):
		if num < 100:
			num += p_list[i]
		else:
			index = i-1
			break

	while (is_prime(num) != True):
		num -= p_list[index]
		index -= 1

	return num

def main():
	print prime_less_million(100)

main()
