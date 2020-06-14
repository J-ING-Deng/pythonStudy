# coding=utf-8
# 去判断用户是否登录成功
db = [
    {"username":"张三","password":"123456"},
    {"username":"李四","password":"654321"}
    ]

zh = input("请输入账号：")
mm = input("请输入密码：")

j = 1
for i in db:
     if zh == i.get("username") and mm == i.get("password"):
        print("登录成功,账号是{}".format(zh))
        break
     elif j<len(db):
         j=j+1
         continue
     else:
         print("账号或密码错误")
    # if zh == i.get("username"):
    #     if mm == i.get("password"):
    #         print("登录成功")
    #         break
    #     else:
    #         print("密码错误")
    # else:
    #     continue
#for循环嵌套
# for i in db:
#     # print(i)    #i是列表中的字典
#     for a in i:
#         print(a)
#         print(i.get(a))
#         print("===========")

