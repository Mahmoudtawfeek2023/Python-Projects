import csv
import docx

# Open the CSV file
with open('passwords.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Create a new Word document
    doc = docx.Document()
    
    # Add a table with headers to the document
    table = doc.add_table(rows=1, cols=2)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Username'
    hdr_cells[1].text = 'Password'
    
    # Add the data to the table
    for row in csv_reader:
        row_cells = table.add_row().cells
        row_cells[0].text = row['Username']
        row_cells[1].text = row['Password']
    
    # Save the document
    doc.save('passwords.docx')