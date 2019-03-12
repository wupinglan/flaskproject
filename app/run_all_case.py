# coding:utf-8
import unittest
import os,sys
sys.path.append(os.path.join(os.path.abspath('.')))
from app import HTMLTestRunnerCN
import time

def runCase(caseName):
    # 用例路径 #获取当前目录下的case测试用例
    case_path = os.path.join(os.path.abspath('.'),"case")
    # 报告存放路径
    # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    report_path = os.path.join(os.path.abspath('.'), "templates/") + caseName +".html"

    # if __name__ == "__main__":
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern=caseName+".py",
                                                    top_level_dir=None)
    fp = open(report_path,"wb") 
    # runner = unittest.TextTestRunner(stream = fp,verbosity=2)
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='自动化测试报告',
        description='详细测试用例结果',
        tester='Findyou'
    )    
    runner.run(discover)
    fp.close()

# runCase('nihao')