
import xlwings as xw

# Connect to the Excel application and open the workbook
app = xw.App(visible=True)
workbook = app.books.open('/Users/ncardona/Desktop/FORMATO ACTUAL PERFILES.xlsx')

# Get the source sheet
source_sheet = workbook.sheets[0]  # Replace 'SourceSheet' with the actual name of the source sheet

# Get the range of data from the source sheet
data_range = source_sheet.range('A1').expand('table')  # Assuming the data starts from cell A1 and forms a table

print(dir( data_range ))
# Get the values from the data range as a matrix
data_matrix = data_range.value

# Create a new target spreadsheet for each row of data
# for row_index, row_data in enumerate(data_matrix):
#     print(row_index, row_data)
#     # Create a new target sheet
#     target_sheet = workbook.sheets.add(name=f'TargetSheet_{row_index+1}')  # Naming each sheet as TargetSheet_1, TargetSheet_2, etc.
#
#     # Write the row data to the target sheet
#     target_sheet.range('A1').value = row_data  # Assuming you want to write the data starting from cell A1 in the target sheet
#
#     # Click the "SIGUIENTE" button
print(source_sheet)
print(dir( source_sheet ))
print(source_sheet.pictures["SIGUIENTE"])
print(source_sheet.shapes["SIGUIENTE"])
# button = source_sheet.buttons['SIGUIENTE']  # Replace 'SIGUIENTE' with the actual name of the button

# button.click()
#
# # Save the workbook and close the Excel application
# workbook.save()
# workbook.close()
# app.quit()
