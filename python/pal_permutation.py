def pal_permutation(string):
	pal_dictionary = {}
	pal_values = []
	odd_counter = 0
	
	string = string.replace(" ", "")	

	for c in string:
		if c in pal_dictionary:
			pal_dictionary[c] += 1
		else:
			pal_dictionary[c] = 1
	
	pal_values = pal_dictionary.values()

	for el in pal_values:
		if el % 2 != 0:
			odd_counter += 1
	
	if odd_counter > 1:
		return False
	else:
		return True

def main():
	string = "rra cic ea"
	boolean = pal_permutation(string)
	print(boolean)

main()
