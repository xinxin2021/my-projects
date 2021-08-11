# coding=utf-8
import time,platform,os
print("------------------------1.当前时间------------------------")
now=time.localtime(time.time())
now=time.strftime("%Y-%m-%d %H:%M:%S",now)
print("当前时间：",now)
print("------------------------2.平台信息------------------------")
print("操作系统：",platform.system())
print("操作系统版本：",platform.version())
print("基于",platform.machine(),"机器的",platform.architecture(),"架构计算机")
print("网络名：",platform.node())
print("处理器：",platform.processor())
print("------------------------3.目录信息------------------------")
print("当前文件系统名称：",os.name)
current=os.getcwd()
print("当前目录：",current)
print("当前目录文件：",os.listdir(current))
print("根目录绝对路径：",os.path.abspath("."))
print("根目录文件：",os.listdir("."))
mtime=time.localtime(os.path.getmtime(current))
mtime=time.strftime("%Y-%m-%d %H:%M:%S",mtime)
print("当前文件夹最后修改时间：",mtime)
print("------------------------4.执行系统命令------------------------")
while True:
    cmd=input("============\n|1.网络信息  |\n|2.画图板    |\n|3.计算器    |\n|4.其他键退出|\n============\n")
    if cmd in ["1","2","3"]:
        if cmd == "1":
            ipcon=os.popen("ipconfig").read()
            print(ipcon)
        if cmd == "2":
            os.popen("mspaint")
        if cmd == "3":
            os.popen("calc")
    else:
        print("输入无效！")
        break



