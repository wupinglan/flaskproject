from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,json
import selenium.webdriver.support.ui as ui
from browsermobproxy import Server 
# driver = webdriver.Firefox()
# driver.get("http://www.ebrun.com/20181211/265539.shtml")
# time.sleep(5)
# test = driver.find_element_by_class_name('cmt-textarea')
# time.sleep(5)
# ActionChains(driver).move_to_element(test).perform()
# time.sleep(5)
# test.click()
# #登录

# time.sleep(5)
# link = driver.find_element_by_id('btn_switch_loginType')
# driver.execute_script('$(arguments[0]).click()', link)

# driver.find_element_by_id('account').send_keys('18610851331')
# driver.find_element_by_id('password').send_keys('wu123456')
# driver.find_element_by_id('btn_login').click()
# # driver.switch_to_default_content()

# test.send_keys('评论测试')
# time.sleep(5)
# driver.find_element_by_class_name('cmt-btn-publish').click()
# time.sleep(5)
# driver.quit()

server = Server("/Users/wupinglan/Desktop/git/flaskproject/browsermob-proxy-2.1.4/bin/browsermob-proxy")
server.start() 
proxy = server.create_proxy() 

profile = webdriver.FirefoxProfile() 
profile.set_proxy(proxy.selenium_proxy()) 
driver = webdriver.Firefox(firefox_profile=profile) 

proxy.new_har("baidu") 
driver.get("http://api.ebrun.com/api/manage/activity/apply-activity-material?meeting_id=1958&luck_draw_id=49&uid&source=H5&name=接口测试吴平兰&phone=18610851331&company=测试&job=测试&email=xiaowuaaaaa@qq.com") 
proxy.wait_for_traffic_to_stop(1, 60) 
with open('/Users/wupinglan/Desktop/git/flaskproject/case/1.har', 'w') as outfile:
    json.dump(proxy.har, outfile) 

server.stop() 
driver.quit() 
