# coding:utf8
import warnings
warnings.filterwarnings("ignore")
import pymysql
import pymysql.cursors
from config import *
import os
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
def insert_testcase(casestep, casedescribe, modulename, modulenumber,Usecasemethod,Usecasefile):
    (db,cursor) = connectdb()
    sql = "insert into testcaseall(casestep, casedescribe, modulename, modulenumber,Usecasemethod,Usecasefile) values(%s, %s, %s,%s, %s,%s)"
    cursor.execute(sql,[casestep, casedescribe, modulename, modulenumber,Usecasemethod,Usecasefile])
    closedb(db,cursor)

#查询所有的用例
def select_testcase():
    (db,cursor) = connectdb()
    sql = "select * from testcaseall"
    cursor.execute(sql)
    select_all_testcase = cursor.fetchall()
    closedb(db,cursor)
    return select_all_testcase

#根据条件查询单个用例
def select_one_testCase(ID):
    (db,cursor) = connectdb()
    cursor.execute('select * from testcaseall where id = %s',ID)
    select_one_testCase =cursor.fetchall()
    closedb(db,cursor)
    return select_one_testCase

#查询某个模块下的用例
def selectModulTestCase(modulenumber_id):
    (db,cursor) = connectdb()
    cursor.execute('select * from testcaseall where modulenumber = %s',modulenumber_id)
    select_modul_testCase =cursor.fetchall()
    closedb(db,cursor)
    return select_modul_testCase

#添加用例表
def update_one_testcase(casestep, casedescribe,modulename, modulenumber,Usecasemethod,Usecasefile,ID):
    print(casestep)
    casestep = '"'+ casestep +'"'
    (db,cursor) = connectdb()
    sql = "UPDATE testcaseall SET casestep=%s, casedescribe='%s', modulename='%s', modulenumber=%s, Usecasemethod='%s', Usecasefile='%s' WHERE id =%s"%(casestep, casedescribe, modulename, modulenumber,Usecasemethod,Usecasefile,ID)
    cursor.execute(sql)
    closedb(db,cursor)

#查询某个模块下的用例
def selectRunTestCase(testClaseId):
    (db,cursor) = connectdb()
    cursor.execute('select * from testcaseall where id = %s',testClaseId)
    selectRunTestCase =cursor.fetchall()
    closedb(db,cursor)
    return selectRunTestCase

def createTestcase(caseNmae,caseValue):
    report_path = os.path.join(os.path.abspath('.'), "case/") + caseNmae +".py"
    with open(report_path, 'w') as f:
        f.write('import unittest')
        f.write('\n')
        f.write('import time')
        f.write('\n')
        f.write('#引入自定义的包')
        f.write('\n')
        f.write('import os,sys')
        f.write('\n')
        f.write("sys.path.append(os.path.join(os.path.abspath('.')))")
        f.write('\n')
        f.write('from app.selenium_api import SeleniumApi')
        f.write('\n')
        f.write('class Test(unittest.TestCase):')
        f.write('\n')
        f.write('    def setUp(self):')
        f.write('\n')
        f.write('        print("start!")')
        f.write('\n')

        f.write('    def tearDown(self):')
        f.write('\n')
        f.write('        print("end!")')
        f.write('\n')
        
        f.write('    def test01(self):')
        f.write('\n')
        f.write('        SeleniumApi.step_startup(self)')
        f.write('\n')
        f.write('        print ("执行测试用例01")')
        f.write('\n')
        f.write("        " + caseValue)
        f.write('\n')
        f.write('        SeleniumApi.step_quit(self)')

#插入测试报告
def insert_testReport(testReportName):
    (db,cursor) = connectdb()
    sql = "insert into testallreport(testReportName) values(%s)"
    cursor.execute(sql,[testReportName])
    closedb(db,cursor)

#查询某个测试报告名称
def selectTestReportName(testReportId):
    (db,cursor) = connectdb()
    cursor.execute('select * from testallreport where id = %s',testReportId)
    selectTestReportName =cursor.fetchall()
    closedb(db,cursor)
    return selectTestReportName

#查询某个测试报告名称
def select_All_Report():
    (db,cursor) = connectdb()
    cursor.execute('select * from testallreport')
    selectAllReport =cursor.fetchall()
    closedb(db,cursor)
    return selectAllReport
