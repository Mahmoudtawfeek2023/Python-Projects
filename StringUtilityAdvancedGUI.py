import sys
import time
import random
import string
import re
import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Playground")
        self.setGeometry(200, 200, 600, 400)
        self.initUI()

    def initUI(self):
        self.font = QFont("Arial", 14)
        self.choice_label = QLabel("Select a function:", self)
        self.choice_label.setFont(self.font)
        self.choice_box = QComboBox(self)
        self.choice_box.setFont(self.font)
        self.choice_box.addItem("Check for the letter 'a' in a name")
        self.choice_box.addItem("Return every other letter of a word")
        self.choice_box.addItem("Reverse the characters of a word")
        self.choice_box.addItem("Create a Spoonerism")
        self.choice_box.addItem("Add exclamation points to strings")
        self.choice_box.addItem("Generate a random password")
        self.choice_box.addItem("Count the number of vowels in a word")
        self.choice_box.addItem("Calculate the factorial of a number")
        self.choice_box.addItem("Calculate the nth number in the Fibonacci sequence")
        self.choice_box.addItem("Calculate the distance between two points in 2D space")
        self.choice_box.currentIndexChanged.connect(self.updateUI)

        self.input_label = QLabel("Enter input:", self)
        self.input_label.setFont(self.font)
        self.input_box = QLineEdit(self)
        self.input_box.setFont(self.font)

        self.output_label = QLabel("Output:", self)
        self.output_label.setFont(self.font)
        self.output_box = QLineEdit(self)
        self.output_box.setFont(self.font)
        self.output_box.setReadOnly(True)

        self.run_button = QPushButton("Run", self)
        self.run_button.setFont(self.font)
        self.run_button.clicked.connect(self.runFunction)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.choice_label)
        main_layout.addWidget(self.choice_box)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_box)
        main_layout.addLayout(input_layout)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_box)
        main_layout.addLayout(output_layout)

        main_layout.addWidget(self.run_button)

        self.setLayout(main_layout)

    def updateUI(self):
        index = self.choice_box.currentIndex()
        if index == 0:
            self.input_label.setText("Enter name:")
        elif index == 1:
            self.input_label.setText("Enter word:")
        elif index == 2:
            self.input_label.setText("Enter word:")
        elif index == 3:
            self.input_label.setText("Enter first word:")
        elif index == 4:
            self.input_label.setText("Enter string:")
        elif index == 5:
            self.input_label.setText("Enter password length:")
        elif index == 6:
            self.input_label.setText("Enter word:")
        elif index == 7:
            self.input_label.setText("Enter number:")
        elif index == 8:
            self.input_label.setText("Enter number:")
        elif index == 9:
            self.input_label.setText("Enter x1, y1, x2, y2 (comma-separated):")

    def runFunction(self):
        index = self.choice_box.currentIndex()
        input_text = self.input_box.text()
        output_text = ""
        if index == 0:
            output_text = check_for_name(input_text)
        elif index == 1:
            output_text = every_other_letter(input_text)
        elif index == 2:
            output_text = reverse_string(input_text)
        elif index == 3:
            output_text = make_spoonerism(input_text)
        elif index == 4:
            output_text = add_exclamation()
        elif index == 5:
            output_text = generate_password(int(input_text))
        elif index == 6:
            output_text = count_vowels(input_text)
        elif index == 7:
            output_text = calculate_factorial(int(input_text))
        elif index == 8:
            output_text = calculate_fibonacci(int(input_text))
        elif index == 9:
            coords = input_text.split(",")
            x1, y1, x2, y2 = [float(coord) for coord in coords]
            output_text = calculate_distance(x1, y1, x2, y2)
        self.output_box.setText(str(output_text))

def check_for_name(name):
    """
    Prompts the user for their name and checks if the name contains a certain letter.
    
    Returns:
    A string containing a message about whether the name contains the letter "a".
    """
    if "a" in name.lower():
        return f"Your name, {name}, contains the letter 'a'."
    else:
        return f"Your name, {name}, does not contain the letter 'a'."

def every_other_letter(word):
    """
    Returns every other letter of a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    A string containing every other letter of the input word.
    """
    return word[::2]

def reverse_string(word):
    """
    Reverses the characters of a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    A string containing the characters of the input word in reverse order.
    """
    return word[::-1]

def make_spoonerism(words):
    """
    Prompts the user for two words and creates a Spoonerism by switching the first letters of the words.
    
    Returns:
    A string containing the two new words separated by a space.
    """
    word1, word2 = words.split(",")
    new_word1 = word2[0] + word1[1:]
    new_word2 = word1[0] + word2[1:]
    return new_word2[0].upper() + new_word1[1:] + " " + new_word1[0].lower() + new_word2[1:]

def add_exclamation():
    """
    Prompts the user to input strings and adds exclamation points to the end of each string until it is 20 characters long.
    
    Returns:
    A list of strings containing the original strings with exclamation points appended to the end if the length is less than 20, or the original strings if the length is already at least 20 characters.
    """
    inputs = []
    while True:
        word = input("Enter a string: ")
        inputs.append(word)
        while len(word) < 20:
            word += "!"
        print(f"Modified string: {word}")
        more_inputs = input("Do you want to add more inputs? (y/n) ")
        if more_inputs.lower() != "y":
            break
    return inputs

def generate_password(length):
    """
    Generates a random password of a given length.
    
    Args:
    length (int): The length of the password to generate.
    
    Returns:
    A string containing a random password of the given length.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def count_vowels(word):
    """
    Counts the number of vowels in a word.
    
    Args:
    word (str): The input word.
    
    Returns:
    An integer representing the number of vowels in the input word.
    """
    vowel_count = 0
    for letter in word:
        if letter.lower() in "aeiou":
            vowel_count += 1
    return vowel_count

def calculate_factorial(num):
    """
    Calculates the factorial of a number.
    
    Args:
    num (int): The input number.
    
    Returns:
    An integer representing the factorial of the input number.
    """
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num-1)

def calculate_fibonacci(n):
    """
    Calculates the nth number in the Fibonacci sequence.
    
    Args:
    n (int): The index of the desired number in the Fibonacci sequence.
    
    Returns:
    An integer representing the nth number in the Fibonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def calculate_distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points in 2D space.
    
    Args:
    x1 (float): The x-coordinate of the first point.
    y1 (float): The y-coordinate of the first point.
    x2 (float): The x-coordinate of the second point.
    y2 (float): The y-coordinate of the second point.
    
    Returns:
    A float representing the distance between the two input points.
    """
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())