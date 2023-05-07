import csv
import json

# Task 1: Import the CSV module
# Done

# Task 2: Create a list of compromised users
compromised_users = []

# Task 3: Open the passwords.csv file
with open('passwords.csv') as password_file:
  
  # Task 4: Parse the CSV file
  password_csv = csv.DictReader(password_file)
  
  # Task 5: Iterate through the CSV file
  for password_row in password_csv:
    
    # Task 6: Print the username
    print(password_row['Username'])
    
    # Task 7: Add the username to the compromised_users list
    compromised_users.append(password_row['Username'])

# Task 8: Open the compromised_users.txt file
with open('compromised_users.txt', 'w') as compromised_user_file:
  
  # Task 9: Iterate over the compromised_users list
  for username in compromised_users:
    
    # Task 10: Write the username to the file
    compromised_user_file.write(username + '\n')

# Task 11: Done

# Task 12: Import the json module
# Done

# Task 13: Open the boss_message.json file
with open('boss_message.json', 'w') as boss_message:
  
  # Task 14: Create a Python dictionary for the boss message
  boss_message_dict = {
    'recipient': 'The Boss',
    'message': 'Mission Success'
  }
  
  # Task 15: Write the dictionary to the JSON file
  json.dump(boss_message_dict, boss_message)

# Task 16: Open the new_passwords.csv file
with open('new_passwords.csv', 'w') as new_passwords_obj:
  
  # Task 17: Write the signature to the file
  slash_null_sig = '''
   _  _     ___   __  ____             
  / )( \   / __) /  \(_  _)            
 ) \/ (  ( (_ \(  O ) )(              
 \____/   \___/ \__/ (__)             
  _  _   __    ___  __ _  ____  ____  
 / )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  '''
  new_passwords_obj.write(slash_null_sig)

# Task 18: Done

# Task 19: Done