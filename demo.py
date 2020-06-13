"""
print("hello world") #字符串
print(2333) #整数
print(2.333)    #小数
print(False)    #布尔值
print(())   #元组
print([])   #数组
print({})   #字典

多行注释

print("哈哈哈",233)
print(("哈哈哈"+"嘻嘻嘻")*100)
print(((1+2)*100-99)/2)
name="张三"
print(name)

print(len("adsfd")) #获取字符串长度

a = float(input("请输入："))    #数据类型的转换

b = float(input("请输入："))

print("输入的内容：",a+b)
print(type(a))   #获取变量数据类型
"""


"""
练习：通过代码获取两段内容，并计算他们长度的和
"""
"""
a = input("请输入第一段内容：")

b = input("请输入第二段内容：")

print("输入的两段内容是：",a+b)

print("两段内容的长度和是：",len(a)+len(b))
"""

"""
#元组,下标，从0开始编号
a = (1,2,3,4,"哈哈","哈哈","嘻嘻","哈哈",True,"哈哈",False)

#访问元组
print(a[5]) #正序
print(a[-1])    #倒序

#查找下标：index()
print(a.index("哈哈"))

#统计元组元素数量
print(a.count("哈哈"))

#切片/截取
print(a[1:5])   #左闭右开区间
print(a[9:])
print(a[:5])

#二维元组
b = (a,"哈哈","嘻嘻")
print(b[0][3])

#元组连接
c = a+b
print(c)

#删除元组
del c
#print(c)
"""

"""
#数组/列表list
#元组和数组/列表list的区别：元组写好后不可修改，数组/列表list则可以
a = [1,2,3,4,"哈哈","哈哈","嘻嘻","哈哈",True,"哈哈",False]
#访问数组/列表list
print(a[4])
print(a[-1])

#查找数组/列表list下标：index()
print(a.index("哈哈"))

#统计数组/列表list元素数量 count()
print(a.count("哈哈"))

#统计数组/列表list长度 len()
print(len(a))

#数组/列表list末尾添加一个元素 append()
a.append("略略略")
print(a[-1])

#数组/列表list插入元素 insert()
a.insert(0,"插入")
print(a[0])

#数组/列表list末尾添加数组/列表list extend()
xx = ["hello","world"]
a.extend(xx)
print(a)

#数组/列表list连接 +
print(a+xx)

#二维元组
b = (a,"哈哈","嘻嘻")
print(b[0][3])

#切片/截取 a[:]
print(a[1:5])   #左闭右开区间
print(a[9:])
print(a[:5])

#剪切 pop()
b = a.pop(3) 
c = a.pop(3)
print(a)
print(b)
print(c)
print(b+c)

#清空 clear()
#a.clear()

#移除数组/列表list中某个值obj的第一个匹配值 remove()
a.remove("哈哈")
del a[1]
print(a)
"""

"""
#注意：
# remove(0)会删除“false”，remove(1)会删除“true”
#下标不要超出范围 == 越界
#ps:a[100]
"""

"""
字段的特点：
1.字典中的值没有顺序
2.字典的接口必须是 键值对的结构 key:value
"""

"""
a = {"name":"张三","sex":"男","age":25}
print(a)
#字典取值
print(a["name"])
print(a.get("name"))
#新增
a["high"] = "175cm"
print(a)
#修改/新增
a["high"] = "178cm"
a.update(name="李四")
a.update(weigh="60kg")
print(a)
#剪切pop()
b = a.pop("weigh")
print(b)
print(a)
#删除字典中某个键值对 del a["key"]
del a["high"]
print(a)
#删除字典 del a
#del a
#清空字典中的所有键值对 clear()
a.clear()
print(a)
"""

"""
获取用户输入的个人信息，并存储到字典中。
个人信息包括了：name,age,sex
"""
a = {}
#a.update(name=input("请输入name:"))
#a.update(age=input("请输入 age:"))
#a.update(sex=input("请输入sex:"))
a["name"] = input("请输入:name:")
a["age"] = input("请输入age:")
a["sex"] = input("请输入sex:")
print(a)
