import pymysql
db = pymysql.connect("localhost","root","qxx120326")
cursor = db.cursor()
sql2="DROP DATABASE IF EXISTS `class`"
answer=input("请再次确认是否删除数据库“class”？(y/n)")
if answer in ["y","Y"]:
    try:
        cursor.execute(sql2)
        print("数据库已不复存在！")
    except:
        print("数据库删除失败！")
else:
    print("删除任务已取消！")
