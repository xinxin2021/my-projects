import pymysql
db = pymysql.connect("localhost","root","qxx120326","class_members",charset='utf8')
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("数据库版本：%s " % data)
db.close()
