from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random




driver = webdriver.Edge()
driver.get("file:///C:/Desenvolvimento/python/teste/index.html")
#driver.get("https://www.instagram.com/viajandoeusoufeliz/")
time.sleep(3)
#acaoPaginaInstagramSeguir()

list = driver.find_elements_by_css_selector("li.wo9IH")
#top = list[7].location["y"]

#driver.execute_script("document.querySelector('div.isgrP').scrollTop=document.querySelectorAll('li.wo9IH')[7].getBoundingClientRect().top")



