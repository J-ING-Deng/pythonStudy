"""
类
    相同属性的集合
    类似修房子的图纸
"""
class Persion():
    #变量：成员变量，类中的变量
    name = "张三"
    sex = "男"
    age = 18

    #功能，成员方法：类中的方法
    def talk(self): #self是成员方法的第一个参数，python的语法要求,self在类内部调用类成员
        print("人能说话")
    
    def eat(self,x):
        print("今晚吃{}".format(x))
    
    def test(self):
        self.talk()

#实例化类：Persion()
p = Persion()
#调用类的属性
print(p.name)
p.talk()
p.eat("鸡")
p.test()