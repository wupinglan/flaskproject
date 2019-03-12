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
        SeleniumApi.step_startup(self)
        print ("执行测试用例01")
        SeleniumApi.step_send_keys(self,'by_name','wd','selenium')
        SeleniumApi.step_quit(self)