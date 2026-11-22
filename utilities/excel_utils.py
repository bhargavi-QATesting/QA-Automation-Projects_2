import openpyxl
#from openpyxl.styles import PatternFill

def getRowCount(file,sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_row

def getColCount(file,sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_column

def readData(file,sheetName,rowCount,colCount):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(rowCount, colCount).value

def writeData(file,sheetName,rowCount,colCount,data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    sheet.cell(rowCount,colCount).value = data
    workbook.save(file)

'''def fillGreenColor(file,sheetName,rowCount,colCount):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    greenFill = PatternFill(
        fill_type='solid',
        fgColor='00FF00'
    )
    sheet.cell(rowCount,colCount).fill = greenFill
    workbook.save(file)

def fillRedColor(file,sheetName,rowCount,colCount):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    redFill = PatternFill(
        fill_type='solid',
        fgColor='FF0000'
    )
    sheet.cell(rowCount,colCount).fill = redFill
    workbook.save(file)'''
