# List comprehension
# [item for item in list if condition]

example_list = ['one', 'two', 'three']
example_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled_list = [number * 2 for number in example_numbers_list]

labeled_list = [
    f"Este es el número: {number}" for number in example_numbers_list]

# print(labeled_list)


# Pares
even_list = [number for number in example_numbers_list if number % 2 == 0]
# Impares
odd_list = [number for number in example_numbers_list if number % 2 != 0]

# print(even_list)
# print(odd_list)


# Para las APIS
user = [user for user in users_list if user["id"] == id]
user = [user for user in users_list if user["id"] != id]
















