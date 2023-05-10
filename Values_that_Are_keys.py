def values_that_are_keys(my_dictionary):
    result = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            result.append(value)
    return result

# Ask the user to input the dictionary
my_dict = {}
while True:
    key = input("Enter a key (press Enter to stop): ")
    if not key:
        break
    value = input(f"Enter a value for key '{key}': ")
    my_dict[key] = value

# Call the function with the user input dictionary
result_list = values_that_are_keys(my_dict)

# Print the resulting list
print("The values that are also keys are:", result_list)