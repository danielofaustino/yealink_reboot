from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
import random
import sys


driver = webdriver.Chrome()

for x in range (15,67):  
  xstr = str(x) 
  ipfinal = "http://192.168.110.14/servlet?m=mod_data&p=settings-upgrade&q=load"
  ipfinal = ipfinal.replace("14",xstr)
  driver.get(ipfinal)
  time.sleep(2)
  user_name_elem = driver.find_element_by_id('idUsername')
  user_name_elem.send_keys("admin")
  passworword_elem = driver.find_element_by_id('idPassword')
  passworword_elem.send_keys("retha@1234")
  passworword_elem.send_keys(Keys.RETURN)
  time.sleep(1)
  reboot_elem = driver.find_element_by_id('PhoneRebootDevice')
  reboot_elem.click()
  time.sleep(1) 
  Alert(driver).accept()
  time.sleep(1) 
 
driver.close()
