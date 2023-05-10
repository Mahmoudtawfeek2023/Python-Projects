def sum_values(my_dictionary):
    total = 0
    for value in my_dictionary.values():
        total += value
    return total

# Ask the user to input the dictionary
my_dict = {}
while True:
    key = input("Enter a key (press Enter to stop): ")
    if not key:
        break
    value = int(input("Enter a value: "))
    my_dict[key] = value

# Call the function with the user input dictionary
result = sum_values(my_dict)

# Print the result
print("The sum of the dictionary values is:", result)