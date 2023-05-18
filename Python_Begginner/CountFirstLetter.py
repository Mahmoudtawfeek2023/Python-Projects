def count_first_letter(names):
    letters = {}
    for last_name in names:
        first_letter = last_name[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[last_name])
    return letters

# Ask the user to input the dictionary
names = {}
while True:
    last_name = input("Enter a last name (press Enter to stop): ")
    if not last_name:
        break
    first_names = input(f"Enter first names for last name '{last_name}' separated by commas: ")
    first_names_list = [name.strip() for name in first_names.split(",")]
    names[last_name] = first_names_list

# Call the function with the user input dictionary
result_dict = count_first_letter(names)

# Print the resulting dictionary
print("The resulting dictionary is:", result_dict)