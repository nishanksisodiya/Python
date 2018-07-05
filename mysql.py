import pymysql

mydb = pymysql.connect(host="localhost",user="nony",passwd="12345",database="library")

myc = mydb.cursor()

sql="use library"

myc.execute(sql)
myc.execute("select book_name,book_sub,count from lib_bookorderhistory")
result = myc.fetchall()
for i in range(0,5):
 print("{0:20d} {1:5d} {2:10d}".format(result[i],result[i],result[i]))