import tkinter as tk
import smtplib

def account_generator(first_name, last_name):
    username = first_name[:3] + last_name[:3]
    return username

def password_generator(first_name, last_name):
    password = last_name[-3:] + first_name[-3:]
    return password

def email_generator(first_name, last_name):
    username = account_generator(first_name, last_name)
    email = username + "@janco.com"
    return email

def generate_account():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    account_name = account_generator(first_name, last_name)
    password = password_generator(first_name, last_name)
    email = email_generator(first_name, last_name)
    account_name_label.config(text="Your account name is: " + account_name)
    password_label.config(text="Your temporary password is: " + password)
    email_label.config(text="Your email address is: " + email)
    send_email(account_name, password, email)

def send_email(account_name, password, email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "mahmoudtawfeek2023@outlook.com" # Replace with your email address
    sender_password = "mah015May2023@VoIS" # Replace with your email password
    recipient_email = "mahmoud.m.tawfeek@gmail.com"
    subject = "Account Information"
    body = f"Your account name is: {account_name}\nYour temporary password is: {password}\nYour email address is: {email}"
    message = f"Subject: {subject}\n\n{body}"
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message)

# Create the main window
window = tk.Tk()
window.title("Account Generator")

# Create the form labels and entry widgets
first_name_label = tk.Label(window, text="Enter your first name:")
first_name_entry = tk.Entry(window)
last_name_label = tk.Label(window, text="Enter your last name:")
last_name_entry = tk.Entry(window)

# Place the form labels and entry widgets in the window
first_name_label.pack()
first_name_entry.pack()
last_name_label.pack()
last_name_entry.pack()

# Create the button to generate the account and password
generate_button = tk.Button(window, text="Generate Account", command=generate_account)
generate_button.pack()

# Create the labels to display the generated account, password, and email address
account_name_label = tk.Label(window, text="")
password_label = tk.Label(window, text="")
email_label = tk.Label(window, text="")
account_name_label.pack()
password_label.pack()
email_label.pack()

# Run the main event loop
window.mainloop()