from mdutils.mdutils import MdUtils
from mdutils.tools.Table import Table

headers = ['ID', 'Name', 'Email', 'Department', 'Salary']
rows = [
    ['1', 'Alice Johnson', 'alice@example.com', 'Engineering', '$95,000'],
    ['2', 'Bob Smith', 'bob@example.com', 'Marketing', '$78,000'],
    ['3', 'Carol Lee', 'carol@example.com', 'Finance', '$88,000'],
    ['4', 'Dave Patel', 'dave@example.com', 'Engineering', '$102,000'],
]



# Create a new markdown file
mdFile = MdUtils(file_name='example', title='My Document')

# Headers
mdFile.new_header(level=1, title='Introduction') 
mdFile.new_paragraph('This is a paragraph of text.')

mdFile.new_header(level=2, title='Lists')

# Unordered list
items = ['First item', 'Second item', 'Third item']
mdFile.new_list(items)

# Bold / italic inline
mdFile.new_paragraph(mdFile.new_inline_link('https://example.com', 'A link'))
# mdFile.new_paragraph(mdFile.new_bold_text('bold') + ' and ' + mdFile.new_italic_text('italic'))

# Table (flat list: headers first, then rows left-to-right)
mdFile.new_header(level=2, title='Table Example')
mdFile.new_table(
    columns=3,
    rows=3,
    text=['Name', 'Age', 'City',
          'Alice', '30', 'NYC',
          'Bob', '25', 'LA']
)

# Table example like the HTML one, see dummy rows at top of file
table_data = headers
for row in rows:
    table_data.extend(row)
mdFile.new_table(columns=5, rows=5, text=table_data)


# Code block
mdFile.new_header(level=2, title='Code')
mdFile.insert_code('print("hello world")', language='python')

# Checkbox list
mdFile.new_header(level=2, title='Tasks')
mdFile.new_checkbox_list(['Done task', 'Pending task', 'Another task'])

# Image
mdFile.new_paragraph(mdFile.new_inline_image('Alt text', 'path/to/image.png'))

# Write the file
mdFile.create_md_file()