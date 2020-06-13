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
a = input("请输入第一段内容：")

b = input("请输入第二段内容：")

print("输入的两段内容是：",a+b)

print("两段内容的长度和是：",len(a)+len(b))