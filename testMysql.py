#coding utf-8
import MySQLdb

conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='test')
cursor = conn.cursor()

sql = 'insert into apple(user,downURL,test) values(%s,%s,%s)'
param = (1,123456,654321)
n = cursor.execute(sql,param)
print n
cursor.execute('commit')
cursor.close()
conn.close()
