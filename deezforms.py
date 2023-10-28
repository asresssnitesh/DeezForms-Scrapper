from selenium import webdriver
from creds import email,password
import deezforms_login as dl


driver = webdriver.Chrome()
linkedin_email = email
linkedin_password = password
dl.login(driver, email, password)
print("logged in")
# person = Person("https://www.linkedin.com/in/sriharshamalla/", driver=driver)


