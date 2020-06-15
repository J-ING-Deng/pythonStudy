class Persion():

    name = "李四"
    #构造方法：__init__，在实例化类的时候给新建/初始化成员变量：固定写法
    def __init__(self,nl):
        self.age = nl   #如果没有该成员变量则新建一个，有就赋值


p = Persion(18) #
print(p.age)