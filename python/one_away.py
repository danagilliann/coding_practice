def one_edit_away(first, second):
	s1 = ""
	s2 = ""
	
	s1 = first if len(first) < len(second) else second
	s2 = second if len(first) < len(second) else first

	i1 = 0
	i2 = 0

	found_difference = False

	while (i2 < len(s2) and i1 < len(s1)):
		if (s1[i1] != s2[i2]):
		
			if (found_difference):
				return False

				'''
					If the program finds another difference
					Then that means it's no longer one edit away
					Therefore, it returns false
				'''
			
			found_difference = True

			# on insert mode
			if (len(s1) < len(s2)): 
				i2 += 1
				
				'''
					In the "pale" and "ple" example, s1 = ple and s2 = pale. 
					So it would go through here.
					It advances the index of s1 so it will continue to match the char of s2
					Go to the comment in 'if found_difference'
				'''
		
		else:
			i1 += 1
			i2 += 1
	
	return True

print one_edit_away("pale","ple")
