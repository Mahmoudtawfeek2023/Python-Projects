def max_key(my_dictionary):
    largest_key = None
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_key = key
            largest_value = value
    return largest_key

# Ask the user to input the dictionary
my_dict = {}
while True:
    key = input("Enter a key (press Enter to stop): ")
    if not key:
        break
    value = float(input(f"Enter a value for key '{key}': "))
    my_dict[key] = value

# Call the function with the user input dictionary
result_key = max_key(my_dict)

# Print the resulting key
print("The key associated with the largest value is:", result_key)