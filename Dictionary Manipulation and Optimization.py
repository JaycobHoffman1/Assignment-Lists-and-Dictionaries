# Task 1
# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. 
# Analyze the time and space complexity of this operation.

def merge_dicts(dict1, dict2):
    return dict1 | dict2

# Task 2
# Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. 
# Analyze the time and space complexity of this operation.

def find_intersection(dict1, dict2):
    intersection = {}
    common_keys = dict1.keys() & dict2.keys()

    for key in common_keys:
        intersection[key] = [dict1[key], dict2[key]]

    return intersection

# Task 3
# Implement a function to count the frequency of each unique word in a list using a dictionary. 
# Analyze the time and space complexity of this operation.

def count_frequency(arr):
    frequency_dict = {}
    
    for ele in arr:
        frequency_dict[ele] = arr.count(ele)

    return frequency_dict