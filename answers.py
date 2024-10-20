#number 1:write a python program to find the maximum of three numbers
def find_maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
#number 2 : write a python progra to sum all the numbers in a list
def sum_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

sample_list = [8, 2, 3, 0, 7]

total_sum = sum_list(sample_list)

print(f"The sum of the numbers in the list is: {total_sum}")
#number 3: write a python program that multiplies all the numbers in a list
def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

sample_list = [8, 2, 3, -1, 7]

total_product = multiply_list(sample_list)

print(f"The product of the numbers in the list is: {total_product}")
#number 4 : write a python program to reverse a string
#sample string:"1234abcd"
def reverse_string(s):
    return s[::-1]

sample_string = "1234abcd"

reversed_string = reverse_string(sample_string)

print(f"The reversed string is: {reversed_string}")

#number 11 : write a python program that checks whether a passed string is a palindrome or not
def is_palindrome(s):


    sample_string = input("Enter a string: ")

if is_palindrome(sample_string):
    print(f"'{sample_string}' is a palindrome.")
else:
    print(f"'{sample_string}' is not a palindrome.")