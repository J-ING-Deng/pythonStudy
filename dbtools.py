import pymysql

def chaxun(sql,h,u,p,d):
    """
        查询mysql数据库
    """
    #pymysql 连接数据库
    db = pymysql.connect(host=h,user=u,password=p,db=d)

    cur = db.cursor()    #获取游标（查询窗口）
    try:
     #执行sql语句
        cur.execute(sql)
        #得到查询结果
        res = cur.fetchall()    #查询结果是元组
    except pymysql.Error as e:
        return e
    finally:
        db.close
    return res

# sql = "select * from t_user where id = 254"
# a = chaxun(sql,"106.53.232.198","root","123456","ljtestdb")
# print(a)

def commit(sql,h,u,p,d):
    """
    插入/修改/删除方法：insert update delete：不要传select
    """
    #连接数据库
    db = pymysql.connect(host=h,user=u,password=p,db=d)
    #获取游标
    cur= db.cursor()
    try:
    #执行sql
        cur.execute(sql)
        db.commit()
        return True
    except pymysql.Error as e:
        db.rollback
        return e
    #提交修改
    finally:
        db.close
    

# sql = "update t_students set s='修改' where id=23"
# sql1 = "select * from t_students where id=23"
# a = commit(sql,"127.0.0.1","root","123456","linqingyang")
# b = chaxun(sql1,"127.0.0.1","root","123456","linqingyang")
# print(a)
# print(b)