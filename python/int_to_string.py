'''
function that converts a string to a number.

"1", "14", "142", "1426", ....
1 = (0) * 10 + 1
14 = 1 * 10 + 4 --> (0) * 10 + 1 ...
142 = (1 * 10 + 4) * 10 + 2
1426 = ((1 * 10 + 4) * 10 + 2) * 10 + 6
'''

def convert_to_number(string): # returns an int 
	multiplier = 0
	int_from_str = 0
	current_char = 0

	for c in string:
		current_char = ord(c)
		current_char -= ord('0')
		
		if multiplier == 0:
			int_from_str = current_char
			multiplier = 10
		else:
			int_from_str = int_from_str * 10 + current_char

	return int_from_str

print (convert_to_number("3333") == 3333)   
