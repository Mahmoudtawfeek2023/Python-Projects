last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[4][1] += 5
grades.remove(85)
grades.append("Pass")
last_semester_gradebook = [["Spanish", 80], ["French", 78], ["Art", 95], ["Music", 88]]

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)