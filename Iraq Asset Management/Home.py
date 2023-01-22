import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("http://iraqasset.scibd.info/Login.aspx")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='tbxLgnUserName']").send_keys("Shyamal.Mondal")
# driver.find_element(By.ID,"password").send_keys("12345678")
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()

# act_title = driver.title
# exp_title = "ASSET MANAGEMENT SYSTEM"

# if act_title == exp_title:
#     print("Login test passed")
# else:
#     print("Login test failed")
time.sleep(3)
driver.close()
