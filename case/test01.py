import unittest
import time
#引入自定义的包
import os,sys
sys.path.append(os.path.join(os.path.abspath('.')))

from app.selenium_api import SeleniumApi
class Test(unittest.TestCase):
    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!") 
        
    def test01(self):
        SeleniumApi.step_startup()
        u'''测试登录用例，账号：xx 密码xx'''
        print ("执行测试用例01")