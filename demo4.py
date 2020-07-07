# while

# a = 1
# while a < 10:
#     print(a)
#     a = a+1



# 作业： 输入账号密码，去判断db中是否含有该账号，如果存在，就修改该账号的密码，
# 如果不存在，就新增一个字典
db = [
    {"username":"tom","password":"123456"},
    {"username":"jack","password":"654321"}
    ]

username = input("请输入账号：")
password = input("请输入密码：")
count = 1
for i in db:
    if username == i.get(username):
        if password != i.get(password):
            i.update(password=password)
            break
    else:
        if count == len(db):
            y = input("该账户不存在，是否注册(y/n):")
            if y == 'y':
                db.append({"username":username,"password":password})
                break
            else:
                break
        else:
            count = count + 1
print(db)