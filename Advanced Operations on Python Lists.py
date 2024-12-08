# Task 1: 
# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, 
# where n is a parameter. Analyze the time and space complexity of this operation.

def create_squares(n):
    return [i**2 for i in range(1, n + 1)]

squares = create_squares(10)

print(f"Task 1: {squares}")

# This function follows O(log n) logarithmic time complexity. As n increases, the time required for the function to create the list increases,
# as does the time required to square each integer element.

# Task 2:
# Implement a function to reverse a sublist within a list from index i to j (inclusive). 
# Analyze the time and space complexity of this operation.

def reverse_sublist(lst, i, j):
    return lst[i:j + 1][::-1]

my_list = [i for i in range(1, 11)]
reversed_sublist = reverse_sublist(my_list, 0, 2)

print(f"Task 2: {reversed_sublist}")

# This function follows O(n) linear time complexity. As the difference between j and i increases,
# the time required for the function to create the sublist increases.

# Task 3:
# Implement a function to merge two sorted lists into a single sorted list. Analyze the time and space complexity of this operation.

def merge_sorted_list(lst1, lst2):
    return sorted(lst1 + lst2)

first_list = [1, 5, 4, 2, 3]
second_list = [7, 9, 8, 6, 10]
sorted_merged_lists = merge_sorted_list(first_list, second_list)

print(f"Task 3: {sorted_merged_lists}")

# This function follows O(n) linear time complexity. As the length of the two lists increases,
# the time required for the function to sort the lists increases.