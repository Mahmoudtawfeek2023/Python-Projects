def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)

# Ask the user to input the dictionary
my_dict = {}
while True:
    key = input("Enter a key (press Enter to stop): ")
    if not key:
        break
    value = input(f"Enter a value for key '{key}': ")
    my_dict[key] = value

# Call the function with the user input dictionary
result_count = unique_values(my_dict)

# Print the resulting count
print("The number of unique values in the dictionary is:", result_count)