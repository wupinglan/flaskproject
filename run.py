# coding:utf8
import os,sys
sys.path.append(os.path.join(os.path.abspath('.')))
from flask import *
from flask import redirect,url_for
import warnings
warnings.filterwarnings("ignore")
import time
from app.py_mysql import *
from app.run_all_case import * 
app = Flask(__name__)
app.config.from_object(__name__)
#首页
@app.route('/',methods = ['GET'])
def index():
    moduleslists=modules_all_select()
    #查询有多少功能模块
    return render_template('index.html',moduleslists=moduleslists)

#填写测试步骤时查询之前填写定位元素值，返回给index页面的js
@app.route('/getjson',methods=['GET','POST'])
def getjson():
    a = request.json
    if a:
        data = a['mod_yongli_num']
        select_yuansu_coo=select_yuansu(data)
        return jsonify(select_yuansu_coo)
    return jsonify('fail')

#模块名称添加
@app.route('/addmodules',methods = ['POST'])
def addmodules():
    data = request.form
    modules_add(data)
    return redirect(url_for('index'))

#模块列表
@app.route('/modules')
def modules():
    return render_template('moduleslists.html')

#测试步骤列表
@app.route('/list/<modulenumber_id>')
def list(modulenumber_id):
    (db,cursor) = connectdb()#链接数据库
    cursor.execute("select * from post where modulenumber = %s",modulenumber_id) #执行sql
    posts = cursor.fetchall() #得到查询数据返回的数据
    for x in range(0,len(posts)):
        #转换timestamp 的时间戳
        posts[x]['timestamp'] = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(int(posts[x]['timestamp'])))
    closedb(db,cursor)
    return render_template('list.html',posts=posts) #把数据返回到前端页面

#展示某条测试步骤详情，修改测试步骤方法
@app.route('/post/<post_id>')
def post(post_id):
    (db,cursor) = connectdb()
    cursor.execute("select * from post where id = %s" ,[post_id])
    post = cursor.fetchone()
    post['timestamp'] = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(int(post['timestamp'])))
    closedb(db,cursor)
    return render_template('post.html',post = post)


#测试步骤处理提交
@app.route('/handle',methods = ['POST'])
def handle():
    data = request.form
    (db,cursor) = connectdb()
    if 'ID' not in data.to_dict().keys():
        cursor.execute("insert into post(modulename, modulenumber, action, testdata, stepdes, lvalue, posmode, elocation, timestamp) values(%s, %s, %s, %s, %s,%s, %s, %s, %s)",[data['modulename'] ,data['modulenumber'] ,data['action'] ,data['testdata'] ,data['stepdes'] ,data['lvalue'] ,data['posmode'] ,data['elocation'] ,int(time.time())])
    else:
        sql = "update post set modulenumber='%s', modulename='%s', action='%s', testdata='%s', stepdes='%s', lvalue='%s', posmode='%s', elocation='%s', timestamp='%s' where id = '%s' "%(data['modulenumber'],data['modulename'], data['action'],data['testdata'],data['stepdes'],data['lvalue'],data['posmode'],data['elocation'],int(time.time()),data['ID'])
        cursor.execute(sql)
    closedb(db,cursor)
    return redirect(url_for('list',modulenumber_id=data['modulenumber']))

#模块列表
@app.route('/modules_all',methods=['GET','POST'])
def modules_all():
    (db,cursor) = connectdb()#链接数据库
    sql = ''' select * from addmodules '''
    cursor.execute(sql) #执行sql
    moduleslists = cursor.fetchall() #得到查询数据返回的数据
    closedb(db,cursor)
    #获取到每个模块有多个元素
    countsyuansu = []
    (db,cursor) = connectdb()
    for itme in moduleslists:
        cursor.execute('select count('+ "'" + itme['modulename'] + "'"+') as '+ "'" + itme['modulename'] + "'"+' from addyuansu where modulename='+"'" + itme['modulename']+"'") #执行sql
        modulescounts = cursor.fetchall() #得到查询数据返回的数据
        for count in modulescounts:
            countsyuansu.append(count[itme['modulename']])
    closedb(db,cursor)
    #获取每个模块有多个测试步骤
    countsyongli = []
    (db,cursor) = connectdb()
    for itme in moduleslists:
        cursor.execute('select count('+ "'" + itme['modulename'] + "'"+') as '+ "'" + itme['modulename'] + "'"+' from post where modulename='+"'" + itme['modulename']+"'") #执行sql
        modulescounts = cursor.fetchall() #得到查询数据返回的数据
        for count in modulescounts:
            countsyongli.append(count[itme['modulename']])
    closedb(db,cursor)

    module_yuansu_yongli_all=[]    
    for index in range(len(moduleslists)):
        itemaa = moduleslists[index]
        countsyuansuhhh = {'countsyuansu':countsyuansu[index],'countsyongli':countsyongli[index]}
        itemaa.update(countsyuansuhhh)
        module_yuansu_yongli_all.append(itemaa)
    return render_template('modules_all.html',module_yuansu_yongli_all=module_yuansu_yongli_all) #把数据返回到前端页面

#添加页面元素
@app.route('/addyuansu',methods = ['POST'])
def addyuansu():
    data = request.form
    (db,cursor) = connectdb()
    cursor.execute("insert into addyuansu(modulename, modulenumber, yuansuname, yuansuvalue) values(%s, %s, %s, %s)",[data['modulename'],data['modulenumber'],data['yuansuname'],data['yuansuvalue']])
    closedb(db,cursor)    
    return redirect(url_for('index')) #把数据返回到前端页面


#元素展示页面
@app.route('/element_all_list/<element_id>',methods=['GET','POST'])
def element_all_list(element_id):
    #获取到每个模块的元素
    (db,cursor) = connectdb()
    cursor.execute('select  * from addyuansu where modulenumber=%s',[element_id])
    # cursor.execute('select  * from addyuansu')
    element_all = cursor.fetchall()
    closedb(db,cursor)
    return render_template('element_all_list.html',element_all=element_all)

#展示某条元素详情，并可进行修改
@app.route('/modify_element/<modify_element_id>',methods=['GET','POST'])
def modify_element(modify_element_id):
    (db,cursor) = connectdb()
    cursor.execute('select * from addyuansu where id=%s',[modify_element_id])
    yuansu_xianqqing = cursor.fetchall()
    closedb(db,cursor)
    element_xianqqing = {}
    for item in yuansu_xianqqing:
        element_xianqqing.update(item)
    return render_template('modify_yuansu.html',yuansu_xianqqing=element_xianqqing)

@app.route('/update_element',methods=['GET','POST'])
def update_element():
    data =request.form
    (db,cursor)=connectdb()
    cursor.execute("update addyuansu set yuansuname='%s',yuansuvalue='%s' where id='%s'" %(data['yuansuname'],data['yuansuvalue'],data['ID']))
    closedb(db,cursor)
    return redirect(url_for('element_all_list',element_id=data['modulenumber']))

#测试用例生成py文件和插入数据库
@app.route('/insert_test_class',methods=['GET','POST'])
def insert_test_class():
    data = request.form
    print(data)
    if 'ID' not in data.to_dict().keys():
        print('没有id')
        insert_testcase(data['casestep'], data['casedescribe'], data['modulename'], int(data['modulenumber']) ,data['Usecasemethod'] ,data['Usecasefile'])
    else:
        print('有id')
        update_one_testcase(data['casestep'], data['casedescribe'], data['modulename'], int(data['modulenumber']) ,data['Usecasemethod'] ,data['Usecasefile'] ,data['ID'])
    return redirect(url_for('test_class_list',select_all_testcase=select_testcase()))

        
#测试用例详情页面
@app.route('/test_class_value',methods=['GET','POST'])
def test_class_value():
    # print(test_class_value)
    return render_template('test_class.html')

#修改某个测试用例
@app.route('/updateClassTest/<classTextId>',methods=['GET','POST'])
def updateClassTest(classTextId):
    # print(test_class_value)
    classTextValue = select_one_testCase(classTextId)
    return render_template('updateClassTest.html',classTextValue=classTextValue)

#所有模块测试用例列表页面
@app.route('/test_class_list',methods=['GET','POST'])
def test_class_list():
    select_all_testcase=select_testcase()
    return render_template('test_class_list.html',select_all_testcase=select_all_testcase)

#某个模块测试用例列表页面
@app.route('/select_modul_testCase/<modulenumber_id>',methods=['GET','POST'])
def select_modul_testCase(modulenumber_id):
    select_modul_testCase=selectModulTestCase(modulenumber_id)
    return render_template('test_class_list.html',select_all_testcase=select_modul_testCase)

#执行selenium代码   
@app.route('/testRun/<testClaseId>')
def testRun(testClaseId):
    print("这是执行测试用例的方法")
    selectRunValue = selectRunTestCase(int(testClaseId))
    print(type(selectRunValue))
    caseNmae = selectRunValue[0]['Usecasefile']
    caseValue = selectRunValue[0]['casestep']
    createTestcase(caseNmae,caseValue)
    runCase(caseNmae)
    insert_testReport(caseNmae+'.html')
    return render_template('testReport.html',selectAllReport=select_All_Report())
    # runCase('nihao')

#测试报告列表
@app.route('/testReport')
def testReport():
    selectAllReport = select_All_Report()
    return render_template('testReport.html',selectAllReport=selectAllReport)

#测试报告详情
@app.route('/details_of_test_report/<report_id>')
def details_of_test_report(report_id):
    report_name = selectTestReportName(int(report_id))
    return render_template(report_name[0]['testReportName'])


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='192.168.3.69', port=8000,debug=True)