"""
    包：
    python 自带的包 time、sys、unittest
    第三方的包 pip/pip3 
        pip -V查看版本 
        pip list 列出以及安装的第三方包
        pip install 安装pip包   
            pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
            pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
            pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple
        pip uninstall 包名 卸载pip包
    自定义包
        把文件夹变成包，可以在不同文件夹下面导入代码
    导入包
        import
        from xxx import 类/变量/方法  from selenium import webdriver
"""
#包的使用，先导入
import time #时间相关 time.sleep(3)
import requests

#导入自定义包
from test.a import aa
print(aa)