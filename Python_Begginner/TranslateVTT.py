import docx

with open("WhatareClassesandObjects-.vtt", "r") as f:
    lines = f.readlines()

# Remove lines that end with "start position:0%" and contain "<"
lines = [line for line in lines if not (line.endswith("start position:0%\n") or "<" in line)]

# Remove repeated lines without changing the order of lines
unique_lines = []
for line in lines:
    if line not in unique_lines:
        unique_lines.append(line)

# Combine lines into a single paragraph and make sure it's in a single line
paragraph = " ".join(unique_lines).replace("\n", " ")

# Write paragraph to Word document
doc = docx.Document()
doc.add_paragraph(paragraph)
doc.save("LessonTranscript.docx")