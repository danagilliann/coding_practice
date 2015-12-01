# returns True if anagrams, False otherwise
def isAnagramOptimized(a, b):
    if len(a) != len(b):
        return False
    
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
    
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True

def anagram_list(anagram):
    new_anagram = []
    
    for x in range(0, len(anagram)):
        for y in range (x+1, len(anagram)):
            if (isAnagramOptimized(anagram[x], anagram[y])) and (anagram[x] not in new_anagram) and (anagram[y] not in new_anagram):
                new_anagram.append(anagram[x])
                new_anagram.append(anagram[y])
    
    return new_anagram

print anagram_list(["man","nam","car","rca", "pink"])
