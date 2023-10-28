from selenium import webdriver
from creds import email,password
import deezforms_login as dl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
linkedin_email = email
linkedin_password = password
dl.login(driver, email, password)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, 'element_id')))
print("logged in")



