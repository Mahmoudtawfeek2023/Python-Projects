def sum_even_keys(my_dictionary):
    total = 0
    for key in my_dictionary:
        if key % 2 == 0:
            total += my_dictionary[key]
    return total

# Ask the user to input the dictionary
my_dict = {}
while True:
    key = input("Enter an integer key (press Enter to stop): ")
    if not key:
        break
    key = int(key)
    value = int(input("Enter a value: "))
    my_dict[key] = value

# Call the function with the user input dictionary
result = sum_even_keys(my_dict)

# Print the result
print("The sum of the values of even keys is:", result)