import pymysql
db = pymysql.connect("localhost","root","qxx120326",db="class_members",charset="utf8")
cursor = db.cursor()
sql3="""CREATE TABLE `student` (
`id` int(11) NOT NULL,
`name` varchar(45) DEFAULT NULL,
`sex` char(1) DEFAULT NULL,
`enterdate` datetime DEFAULT NULL,
`department` varchar(45) DEFAULT NULL,
`others` varchar(45) DEFAULT NULL,
PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
try:
    cursor.execute(sql3)
    print("数据表创建成功")
except:
    print("数据表创建失败")
db.close()
