def contains_duplicate(nums):
    dictionary = {}
    for i in nums:
        if i in dictionary.keys():
            return True
        else:
            dictionary[i] = 1
    return False

nums = [2,4,5,6,6,7,3,2,4,9]
print contains_duplicate(nums)
