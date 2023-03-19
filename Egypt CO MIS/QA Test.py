import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj)

driver = webdriver.Chrome()

driver.get("https://egyptcomis.scibd.info/Account/Login")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("cpcaseworker")
driver.find_element(By.ID,"Password").send_keys("12345")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

act_title = driver.title
exp_title = "Beneficiary Information"

if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
time.sleep(5)

driver.close()
