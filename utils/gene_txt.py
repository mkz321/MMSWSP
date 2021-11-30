import sys
import xlrd

book = xlrd.open_workbook(r'C:\Users\39061\Desktop\all_data.xlsx')
sheet = book.sheet_by_index(5) #第几个表
countRow = sheet.nrows
f=open(r'C:\Users\39061\Desktop\246.txt','w')
for i in range(0,countRow,24):  #range(1,countRow,24)
    listRow = sheet.row(i)
    getspeed = listRow[24].value
    getBigindex = listRow[8].value
    getSmallindex = listRow[23].value
    getID = listRow[28].value
    getsb = listRow[18].value
    ss='%f,%f,%f,%f,%f\n' % (getspeed,getSmallindex,getID,getsb,getBigindex)
    #ss='%f,%f,%f,%f\n' % (getspeed,getSmallindex,getID,getsb)
    #ss='%f,%f\n' % (getspeed,getsb)
    f.write(ss)
f.close()