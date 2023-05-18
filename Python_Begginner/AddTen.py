def add_ten(my_dictionary):
    for key in my_dictionary:
        my_dictionary[key] += 10
    return my_dictionary

# Ask the user to input the dictionary
my_dict = {}
while True:
    key = input("Enter a key (press Enter to stop): ")
    if not key:
        break
    value = int(input("Enter an integer value: "))
    my_dict[key] = value

# Call the function with the user input dictionary
modified_dict = add_ten(my_dict)

# Print the modified dictionary
print("The modified dictionary is:", modified_dict)