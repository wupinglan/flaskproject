from selenium import webdriver
import time
class SeleniumApi(object):
    def step_startup():
        driver = webdriver.Firefox()
        driver.get("http://www.baidu.com")

    #对元素进行点击 方法   
    def step_click(self,by_mode,by_value):
        if by_mode =='by_xpath':
            self.driver.find_element_by_xpath(by_value).click()
        elif by_mode == 'by_id':
            self.driver.find_element_by_id(by_value).click()
        elif by_mode == 'by_name':
            self.driver.find_element_by_name(by_value).click()
        elif by_mode == 'by_class_name':
            self.driver.find_element_by_class_name(by_value).click()
        elif by_mode == 'by_tag_name':
            self.driver.find_element_by_tag_name(by_value).click()
        elif by_mode == 'by_link_text':
            self.driver.find_element_by_link_text(by_value).click()
        elif by_mode == 'by_partial_link_text':
            self.driver.find_element_by_partial_link_text(by_value).click()
        elif by_mode == 'by_css_selector':
            self.driver.find_element_by_css_selector(by_value).click()
        else:
            return '你的定位不被支持'
    #该方法是对元素进行输入值
    def step_send_keys(self,by_mode,by_value,send_value):
        if by_mode =='by_xpath':
            self.driver.find_element_by_xpath(by_value).send_keys(send_value)
        elif by_mode == 'by_id':
            self.driver.find_element_by_id(by_value).send_keys(send_value)
        elif by_mode == 'by_name':
            self.driver.find_element_by_name(by_value).send_keys(send_value)
        elif by_mode == 'by_class_name':
            self.driver.find_element_by_class_name(by_value).send_keys(send_value)
        elif by_mode == 'by_tag_name':
            self.driver.find_element_by_tag_name(by_value).send_keys(send_value)
        elif by_mode == 'by_link_text':
            self.driver.find_element_by_link_text(by_value).send_keys(send_value)
        elif by_mode == 'by_partial_link_text':
            self.driver.find_element_by_partial_link_text(by_value).send_keys(send_value)
        elif by_mode == 'by_css_selector':
            self.driver.find_element_by_css_selector(by_value).send_keys(send_value)
        else:
            return '你的定位不被支持'

    #该方法是获取元素对应的值
    def step_text(self,by_mode,by_value):
        if by_mode =='by_xpath':
            ele_results = self.driver.find_element_by_xpath(by_value).text
            return ele_results
        elif by_mode == 'by_id':
            ele_results = self.driver.find_element_by_id(by_value).text
            return ele_results
        elif by_mode == 'by_name':
            ele_results = self.driver.find_element_by_name(by_value).text
            return ele_results
        elif by_mode == 'by_class_name':
            ele_results = self.driver.find_element_by_class_name(by_value).text
            return ele_results
        elif by_mode == 'by_tag_name':
            ele_results = self.driver.find_element_by_tag_name(by_value).text
            return ele_results
        elif by_mode == 'by_link_text':
            ele_results = self.driver.find_element_by_link_text(by_value).text
            return ele_results
        elif by_mode == 'by_partial_link_text':
            ele_results = self.driver.find_element_by_partial_link_text(by_value).text
            return ele_results
        elif by_mode == 'by_css_selector':
            ele_results = self.driver.find_element_by_css_selector(by_value).text
            return ele_results
        else:
            return '你的定位不被支持'
        
    #对元素的输入进行清空  
    def step_clear(self,by_mode,by_value):
        if by_mode =='by_xpath':
            self.driver.find_element_by_xpath(by_value).clear()
        elif by_mode == 'by_id':
            self.driver.find_element_by_id(by_value).clear()
        elif by_mode == 'by_name':
            self.driver.find_element_by_name(by_value).clear()
        elif by_mode == 'by_class_name':
            self.driver.find_element_by_class_name(by_value).clear()
        elif by_mode == 'by_tag_name':
            self.driver.find_element_by_tag_name(by_value).clear()
        elif by_mode == 'by_link_text':
            self.driver.find_element_by_link_text(by_value).clear()
        elif by_mode == 'by_partial_link_text':
            self.driver.find_element_by_partial_link_text(by_value).clear()
        elif by_mode == 'by_css_selector':
            self.driver.find_element_by_css_selector(by_value).clear()
        else:
            return '你的定位不被支持'
    #等待时间
    def step_clear(self,by_time):
        self.time.sleep(by_time)

    def step_quit(self):
        self.driver.quit()
        