from tkinter import filedialog as fd

import openpyxl

def open_file():
    file_path = fd.askopenfilename(
            title="Select file",
            filetypes=[("Excel files", "*.xlsx")]
            )

    work_book = openpyxl.load_workbook(file_path)
    sheet_obj = work_book.active

    file_name = file_path.split("/")[-1]
    headers = [cell.value for cell in sheet_obj[1]]
    full_data = []

    for row in range(sheet_obj.max_row)[2:]:
        row_data = [cell.value for cell in sheet_obj[row]] 

        if is_empty_list(row_data):
            full_data.append(row_data)

    return (file_name, headers, full_data)

def is_empty_list(lst):
    for e in lst:
        if e:
            return False
    return True
