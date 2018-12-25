'''无头浏览器测试'''
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
fireFoxOptions = webdriver.FirefoxOptions() 
fireFoxOptions.set_headless() 
brower = webdriver.Firefox(firefox_options=fireFoxOptions)

# browser = webdriver.firefox()
brower.get('http://www.baidu.com')
print(brower.title)
brower.close()