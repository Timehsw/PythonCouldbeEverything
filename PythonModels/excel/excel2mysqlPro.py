
#encoding=utf-8
import xlrd
import MySQLdb
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
class excel2mysql(object):
    def __init__(self,excelPath):
        self.book = xlrd.open_workbook(excelPath)
        self.sheets=self.book.sheet_names()
        self.database = MySQLdb.connect (host="localhost", user = "root", passwd = "hushiwei", db = "bigdata",charset="utf8")
        self.cursor = self.database.cursor()


    def eachSheets(self):
        for sheetname in self.sheets:
            self.createTable(sheetname)
            self.insertData2MySQL(sheetname)
            print "%s over..." % sheetname
        #     test sheet[0]
        # self.createTable(self.sheets[0])
        # self.insertData2MySQL(self.sheets[0])
        self.end()

    def createTable(self,sheetname):
        sheet=self.book.sheet_by_name(sheetname)
        col=[]
        for r in range(sheet.ncols):
            # col.append("`"+sheet.cell_value(0,r)+"`"+" VARCHAR(200) CHARACTER SET utf8 COLLATE utf8_general_ci ,")
            col.append("`"+sheet.cell_value(0,r)+"`"+" TEXT ,")
        tablename="".join(col)
        self.cursor.execute("DROP TABLE IF EXISTS %s " % sheetname)
        tmp = """CREATE TABLE `"""+sheetname+"""` ("""+tablename+""")"""
        sql=tmp[0:-2]+") ENGINE=InnoDB DEFAULT CHARSET=utf8"
        # print sql
        self.cursor.execute(sql)
        self.database.commit()

    def insertData2MySQL(self,sheetname):
        sheet=self.book.sheet_by_name(sheetname)
        col=[]
        for r in range(sheet.ncols):
            col.append("`"+sheet.cell_value(0,r)+"`")
        str=",".join(col)
        for r in range(1,sheet.nrows):
            arr=[]
            for c in range(0,sheet.ncols):
                arr.append(" '%s'"% (sheet.cell(r,c).value))
            # print "---------------------------------------------"
            value=",".join(arr)
            sql="""INSERT INTO `"""+sheetname +"""` ("""+str+""") VALUES ("""+value+""")"""
            # print sql
            self.cursor.execute(sql)
            del arr

    def end(self):
        self.database.commit()
        self.cursor.close()
        self.database.close()
        print "Over ... "
if __name__ == '__main__':

    # excelPath='/home/devel/ouyedata/demoexcel.xls'
    excelPath='/home/hushiwei/Documents/demoexcel.xls'
    app=excel2mysql(excelPath=excelPath)
    app.eachSheets()