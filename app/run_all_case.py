# coding:utf-8
import unittest
import os
import html_test_runner
# 用例路径 #获取当前目录下的case测试用例
case_path = os.path.join(os.path.abspath('.'),"case")
# 报告存放路径
report_path = os.path.join(os.path.abspath('.'), "templates") + "/test.html"
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    fp = open(report_path, 'wb')
    runner = html_test_runner.HTMLTestRunner(
                    stream=fp,
                    title='My unit test',
                    description='This demonstrates the report output by HTMLTestRunner.'
                    )
    runner.run(all_case())    
    fp.close()   