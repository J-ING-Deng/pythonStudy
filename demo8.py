"""
pymysql
    使用python连接并且查询mysql数据库
"""

"""
    模拟管理员登录
"""
import time
from dbtools import chaxun
from dbtools import commit
# username = input("请输入你的账号：")
# password = input("请输入密码：")

# sql = 'select * from t_admin where username="{}" and password="{}"'.format(username,password)
# res = chaxun(sql,"106.53.232.198","root","123456","ljtestdb")

# if isinstance(res,tuple):   #判断res是否为元组类型
#     if len(res) != 0:
#         print("登录成功！")
#     else:
#         print("账号或密码错误")
# else:    
#     print(res)


"""
    模拟注册
"""

username = input("请输入你的账号：")
password = input("请输入密码：")
t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
sql = "INSERT INTO `tb_account`(`LOGIN_NAME`, `LOGIN_PASSWORD`, `CREATE_DATE`,`USER_NAME`, `USER_IDENTITY`, `PIC_IMG`, `EMAIL`, `TELEPHONE`, `SEX`, `AGE`, `PAYMENT`,`USER_POINT`, `MSG_NUM`, `STATUS`, `LAST_LOGIN_TIME`, `LAST_LOGIN_IP`) VALUES ( '{}', '{}', '{}', '李四', '441823198505053695', NULL, '15622558635@163.com', '15622558656', 0, 0, 0, 0, 0, 0, NULL, NULL)".format(username,password,t)
res = commit(sql,"127.0.0.1","root","123456","db_morning")

if res == True:   #判断res是否为元组类型
    print("注册成功！")
    sql1 = "select * from tb_account where LOGIN_NAME='{}'".format(username)
    res1 = chaxun(sql1,"127.0.0.1","root","123456","db_morning")
    if isinstance(res1,tuple):   #判断res是否为元组类型
        if len(res1) != 0:
            print(res1)
        else:
            print("但是数据库中似乎没有这个新增账号哦")
    else:    
        print(res1)
else:    
    print(res)

