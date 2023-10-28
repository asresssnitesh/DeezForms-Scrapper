
from selenium import webdriver
# from linkedin_scraper import Person, action
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from creds import email,password


options = webdriver.ChromeOptions()

actions.login(options, email, password) 

service = Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.linkedin.com/in/sriharshamalla/n")
time.sleep(1000)
