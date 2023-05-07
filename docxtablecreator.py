import docx

# Define the data as a list of tuples
data = [
    ('Roger Smith', 'rsmith', 'wigginsryan@yahoo.com'),
    ('Michelle Beck', 'mlbeck', 'hcosta@hotmail.com'),
    ('Ashley Barker', 'a_bark_x', 'a_bark_x@turner.com'),
    ('Lynn Gonzales', 'goodmanjames', 'lynniegonz@hotmail.com'),
    ('Jennifer Chase', 'chasej', 'jchase@ramirez.com'),
    ('Charles Hoover', 'choover', 'choover89@yahoo.com'),
    ('Adrian Evans', 'adevans', 'adevans98@yahoo.com'),
    ('Susan Walter', 'susan82', 'swilliams@yahoo.com'),
    ('Stephanie King', 'stephanieking', 'sking@morris-tyler.com'),
    ('Erika Miller', 'jessica32', 'ejmiller79@yahoo.com')
]

# Create a new Word document
doc = docx.Document()

# Add a table to the document
table = doc.add_table(rows=1, cols=3)
table.style = 'Table Grid'

# Add the header row
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Name'
hdr_cells[1].text = 'Username'
hdr_cells[2].text = 'Email'

# Add the data rows
for name, username, email in data:
    row_cells = table.add_row().cells
    row_cells[0].text = name
    row_cells[1].text = username
    row_cells[2].text = email

# Save the document
doc.save('output.docx')