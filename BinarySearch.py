"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    n = len(input_array)
    min_index =0
    max_index =n-1
    current_index = n//2
    while True:
        current_value = input_array[current_index]
        if(current_value == value):
            return current_index
        if(min_index == max_index):
            break
        if current_value > value:
            max_index = current_index -1
        else:
            min_index = current_index + 1
        current_index = (min_index + max_index)//2
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))