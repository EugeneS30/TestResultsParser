'''
Created on 27 May 2015

@author: Eugene Shragovich
'''

from datetime import datetime
from lib import xlwt

from generics.Logger import logging

class ExcelWriter(object):
    '''
    classdocs
    '''
    
    def __init__(self, sheetName):
        self.workbook = xlwt.Workbook()
        self.worksheet = self.workbook.add_sheet(sheetName)
        self.styleHeading = xlwt.easyxf('font: name Arial, color-index blue, bold 1')#, num_format_str='#,##0.00')
    
    def writeLine(self, textData, row, col, style=None):
        if style == None:
            self.worksheet.write(row, col, textData)
        elif style == "heading":
            self.worksheet.write(row, col, textData, self.styleHeading)
        
    def saveFile(self, fileName="TestResults"):
        try:
            #self.workbook.save(fileName + datetime.now().strftime("_%d-%m-%y") + ".xls")
            self.workbook.save(fileName + ".xls")
            logging.info("File saved")
        except IOError:
            logging.error("Cannot save file!")
            logging.error("Make sure the file is not locked!")
            exit(1)
        
    @DeprecationWarning    
    def test(self):
        self.worksheet.write(0, 0, 1234.56)#, style0)
        self.worksheet.write(1, 0, "datetime.now()")#), style1)
        self.worksheet.write(2, 0, 1)
        self.worksheet.write(2, 1, 1)
        self.worksheet.write(2, 2, xlwt.Formula("A3+B3"))