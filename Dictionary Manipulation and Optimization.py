# Task 1
# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. 
# Analyze the time and space complexity of this operation.

def merge_dicts(dict1, dict2):
    return dict1 | dict2

about_jaycob = {
    "name": "Jaycob",
    "age": 20,
    "likes": ["animals", "rollercoasters", "being outside"]
}

about_joshy = {
    "name": "Joshy",
    "age": 13,
    "dislikes": ["string cheese", "rain", "spiders"]
}

merged_dict = merge_dicts(about_jaycob, about_joshy)

print(f"Task 1: {merged_dict}")

# This function follows an O(n) linear time complexity. 
# As the length of the dictionaries increases, the time required to merge the two dictionaries increases.

# Task 2
# Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values. 
# Analyze the time and space complexity of this operation.

def find_intersection(dict1, dict2):
    intersection = {}
    common_keys = dict1.keys() & dict2.keys()

    for key in common_keys:
        intersection[key] = [dict1[key], dict2[key]]

    return intersection

intersection = find_intersection(about_jaycob, about_joshy)

print(f"Task 2: {intersection}")

# This function follows an O(n) linear time complexity.
# As the length of the dictionaries increases, the time required to find common elements between them increases as well.

# Task 3
# Implement a function to count the frequency of each unique word in a list using a dictionary. 
# Analyze the time and space complexity of this operation.

def count_frequency(arr):
    frequency_dict = {}
    
    for ele in arr:
        frequency_dict[ele] = arr.count(ele)

    return frequency_dict

words = ["cat", "rat", "cat", "bat", "hat", "cat", "bat", "rat", "hat", "cat", "rat"]

frequency_dict = count_frequency(words)

print(f"Task 3: {frequency_dict}")

# This function follows an O(n) linear time complexity.
# As the length of the list increases, the time required to loop through it increases.