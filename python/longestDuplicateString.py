input = "abcdjhdeejklkolklklpp" # --> klk
lklklpp" # --> klk


def longestDuplicateSubstring(input):
       pass
    
def substringCounts(input):
    
    if len(input) == 1:
        return input
    
    longest_duplicate = [input[0], 1]
    substring_dict = {}
    midpoint = (len(input)-1)/2
    
    while midpoint > -1:
        
        start = 0
        end = midpoint
        
        while end != len(input):
            
            substring = input[start:end+1]
        
            if (substring not in substring_dict.keys()):
                substring_dict[substring] = 1
            else:
                substring_dict[substring] += 1
    
            start += 1
            end += 1
    
        midpoint -= 1
        
    
    for key, value in substring_dict.iteritems():
            
        if len(longest_duplicate[0]) <= len(key) and value > 1:
            
            longest_duplicate[0] = key
            longest_duplicate[1] = value
            
    
    return longest_duplicate[0]
    
    
print substringCounts(input)


 longestDuplicateSubstring(input):
       pass
    
def substringCounts(input):
    
    if len(input) == 1:
        return input
    
    longest_duplicate = [input[0], 1]
    substring_dict = {}
    midpoint = (len(input)-1)/2
    
    while midpoint > -1:
        
        start = 0
        end = midpoint
        
        while end != len(input):
            
            substring = input[start:end+1]
        
            if (substring not in substring_dict.keys()):
                substring_dict[substring] = 1
            else:
                substring_dict[substring] += 1
    
            start += 1
            end += 1
    
        midpoint -= 1
        
    
    for key, value in substring_dict.iteritems():
            
        if len(longest_duplicate[0]) <= len(key) and value > 1:
            
            longest_duplicate[0] = key
            longest_duplicate[1] = value
            
        
    return longest_duplicate[0]
    
    
print substringCounts(input)


