import xlrd
from tkinter import filedialog as fd

def open_file():
    file_path = fd.askopenfilename(
            title="Select file",
            filetypes=[("Excel files", "*.xlsx")]
            )
    work_book = xlrd.open_workbook(file_path)
    sheet = work_book.sheet_by_index(0)

    file_name = file_path.split("/")[-1]
    headers = [str(cell.value) for cell in sheet.row(0)]
    people = []

    for row in range(sheet.nrows)[1:]:
        person = []
        for cell in sheet.row(row):
            try:
                person.append(int(cell.value))
            except ValueError:
                person.append(str(cell.value))

        people.append(person)

    return (file_name, headers, people)
