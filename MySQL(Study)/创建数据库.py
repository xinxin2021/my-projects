import pymysql
db = pymysql.connect("localhost","root","qxx120326")
cursor = db.cursor()
sql1="CREATE DATABASE IF NOT EXISTS `class_members`"
try:
    cursor.execute(sql1)
    print("数据库创建成功")
except:
    print("数据库创建失败")
db.close()
