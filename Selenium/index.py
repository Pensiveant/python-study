from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

browser= webdriver.Chrome()
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')

time.sleep(2)
input=driver.find_elements_by_css_selector('input.s_ipt')[0]
input.send_keys('selenium')
searchBtn=driver.find_elements_by_css_selector('.s_btn')[0]
driver.find_element_by_tag_name
searchBtn.click()
driver.close()
