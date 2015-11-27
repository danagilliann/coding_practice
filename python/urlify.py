def urlify(string, length):
	replacement = "%20"
	str_list = list(string)
	
	print(str_list)

	for i in range(0, length-1):
		if str_list[i] == " ":
			str_list[i] = replacement

	return "".join(str_list)

def main():
	string = "hello there friend" 
	print(urlify(string, len(string)))

main()
