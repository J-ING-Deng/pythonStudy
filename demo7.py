"""
方法：
    为了代码复用
"""

#def 固定方法定义格式
# a,b 形参
# return 返回值
def sum(a,b):
    return a+b

def test(i=10):  #給参数设置默认值
    print(i)
def test1(): #多个返回值
    return 10,20,30

test()
a,b,c = test1()
print(a)
print(sum(3,4))