import pymysql
import copy
import datetime
a={1:[1,'男']}
for i in a:
    if a[i]==[1,'男']:
        print(i)

MysqlDatabase = pymysql.connect(host='192.168.7.31',port=3306,user='ngoss_dim',passwd='ngoss_dim')
MysqlCursor=MysqlDatabase.cursor()
UseDatabase='label_support'
#MysqlCommand = "select BatchMap,ClassifyValueMap from %s.ResultPersonNumber;" % UseDatabase
MysqlCommand = "show databases;"
MysqlCursor.execute(MysqlCommand)
BatchAndValueMapTupleList = MysqlCursor.fetchall()
print(BatchAndValueMapTupleList)

MysqlCommand = "use %s;"  % UseDatabase
MysqlCursor.execute(MysqlCommand)
MysqlCommand = "show tables;"
MysqlCursor.execute(MysqlCommand)
BatchAndValueMapTupleList = MysqlCursor.fetchall()
print(BatchAndValueMapTupleList)
for table in BatchAndValueMapTupleList:
    print(table[0])




'''
def GetTodayDateTime():
    Today=datetime.datetime.now()
    print(Today)
    #time1 = datetime.datetime.strptime(Today, '%Y-%m-%d %H:%M:%S')  # 字符串转化为datetime
    time1 = datetime.datetime.strftime(Today, '%Y-%m-%d %H:%M:%S')  # datetime转化为字符串
    DateTime = datetime.datetime.strftime(Today, '%Y-%m-%d')
    print(time1)
    print(DateTime)
GetTodayDateTime()
'''