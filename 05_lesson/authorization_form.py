from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/login")

#Ввод зачения в поле username
input = driver.find_element(By.ID, "username")
input.send_keys("tomsmith")
sleep(3)

#Ввод значниея в поле password
input = driver.find_element(By.ID, "password")
input.send_keys("SuperSecretPassword!")
sleep(3)

#Нажать на кнопку Login
button = driver.find_element(By.TAG_NAME, "button")
button.click()
sleep(3)

#Закрыть браузер
driver.close()