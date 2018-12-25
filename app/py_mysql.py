# coding:utf8
import warnings
warnings.filterwarnings("ignore")
import pymysql
import pymysql.cursors
from config import *
# 连接数据库
def connectdb():
    db = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD, db=DATABASE, port=PORT, charset=CHARSET, cursorclass=pymysql.cursors.DictCursor)
    db.autocommit(True)
    cursor = db.cursor()
    return(db,cursor)

# 关闭数据库
def closedb(db,cursor):
    db.close()
    cursor.close()

#查询有多少功能模块
def modules_all_select():
    (db,cursor) = connectdb()#链接数据库
    cursor.execute("select * from addmodules") #执行sql
    moduleslists = cursor.fetchall() #得到查询数据返回的数据
    closedb(db,cursor)
    return moduleslists

#添加功能模块    
def modules_add(data):
    (db,cursor) = connectdb()
    cursor.execute("insert into addmodules(modulename, modulenumber, pagename, casename) values(%s, %s, %s,%s)",[data['modulename'],data['modulenumber'],data['modulename']+'页面元素',data['modulename']+'测试用例'])
    closedb(db,cursor)

#查询元素列表
def select_yuansu(yuansuvalue):
    (db,cursor) = connectdb()
    cursor.execute('select * from addyuansu where modulenumber = %s',yuansuvalue)
    select_yuansu_all =cursor.fetchall()
    closedb(db,cursor)
    return select_yuansu_all
#添加用例表
def insert_testcase(casestep, describecase, modulename, modulenumber):
    (db,cursor) = connectdb()
    sql = "insert into TestCase(casestep, describecase, modulename, modulenumber) values(%s, %s, %s,%s)"
    cursor.execute(sql,[casestep, describecase, modulename, modulenumber])
    closedb(db,cursor)