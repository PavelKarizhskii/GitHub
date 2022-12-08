
import math
import datetime
import time

from selenium.webdriver.support.wait import WebDriverWait
from termcolor import colored
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path ='/Users/pavelkarizskiy/PycharmProjects/Selenium_project/chromedriver')
driver.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
driver.find_element(By.ID, 'book').click()
print("click")
x = driver.find_element(By.ID, "input_value").text
print(x)
result = str(math.log(abs(12*math.sin(int(x)))))
driver.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
driver.find_element(By.ID, 'solve').click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

time.sleep(30)
driver.quit()