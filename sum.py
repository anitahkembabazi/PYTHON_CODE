#LISTS
#number one 
#write a python program to sum all the items in a list
def sum_of_list(items):
    total = 0
    for item in items:
        total += item
    return total
# number 2:write a python program to multiply all the items in a list
def multiply_items(items):
    total =1
    for item in items:
        total *= item
    return total
#number 3: write a python program to get the largest number from a list
def largest_number(items):
    largest = items[4]#assuming the 3rd item is the largest
    for item in items:
        if item > largest:
            largest = item
    return largest
#number 4: write a python program to get the smallest number from a list
def smallest_item(items):
    smallest = items[3]#assuming the smallest item is the second item
    for item in items:
        if item < smallest:
            smallest = item
    return smallest
#number 7: write a python program to remove duplicates from a list.
def remove_duplicates(list2):
    return list(set(list2))
#number 8: write a python program to check if a list is empty or not
def empty_list(items):
    if not items:
        return None
#number 9:Write a python program to clone or copy a list
def clone_list(original_list):
    return original_list.copy()
#number20: write a python program to convert a list of characters into a string
def convert_list_to_sting(list_characters):
    return''.join(list_characters)
#number 21 :write a python program to append a list to the second list
def append_list(list1, list2):
    return list1 + list2
#number 27: write a python program to get the frequency of elements in a list
def frequency_of_elements(items):
    frequency = {}
    for item in items:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency=1
    return frequency

#DICTIONARIES
#number 9:write a python program that sums all the items in a dictionary
def sum_items(dictionary):
    return sum(dictionary.values())
#number 10: write a python program that multiplies all the items in a dictionary
def product_of_items(dictionary):
    result = 1
    for value in dictionary.values():
        result*=value
    return result

#TUPLES
# number1: write a program to create tuples   
def create_tuple(*elements):
    return tuple(elements)
#number 5:write a program to add an item to a tuple
def add_item_to_tuple(tpl, item):#by concatenating 
    new_tuple= tpl + (item,)
    return new_tuple

#SETS
#number 1: write a program to create a set:
def create_set(*elements):
    return set(elements)
#number 2:
def add_members_to_set(s, *members):
    for member in members:
        s.add(member)
    return s
