import docx 
import json


with open('../data/test.json', 'r') as f:
    data = json.load(f)

lst = []
for key in data:
    if key != 'path':
        for in_key in data[key]:
            lst.append([in_key, str(data[key][in_key]).replace("'", '').\
                        replace('{', '').replace('}', '')])

doc = docx.Document()

table = doc.add_table(rows=2, cols=2)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Раздел'
hdr_cells[1].text = 'Описание'

for row in lst:
    row_cells = table.add_row().cells
    for i in range(len(row)):
        row_cells[i].text = row[i]

doc.add_page_break()
doc.save("../data/test.docx")