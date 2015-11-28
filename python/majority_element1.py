'''
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''

def majority_element(arr):
        majority = len(arr)/2
        arr_dict = {} # counts the number of appearances
        
        for x in arr:
                if (x in arr_dict.keys()):
                        arr_dict[x] += 1
                else:
                        arr_dict[x] = 1

        for k in arr_dict.keys():
                if arr_dict.get(k) > majority:
                        return k

print majority_element([1,3,3,4,5,3,3,3,3])
