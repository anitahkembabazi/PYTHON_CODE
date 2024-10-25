def multiply_list(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

sample_list = [8, 2, 3, -1, 7]

total_product = multiply_list(sample_list)

print(f"The product of the numbers in the list is: {total_product}")