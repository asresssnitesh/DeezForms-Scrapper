from selenium import webdriver
from creds import email,password
import deezforms_login as dl
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from deezforms_linkdin import scrape_profile

print(scrape_profile('https://www.linkedin.com/in/sriharshamalla/'))



