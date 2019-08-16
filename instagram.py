from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys

def buscarSeguidores(perfil):
    try:
        init()
        abrirPerfil(perfil)
        element = driver.find_element_by_xpath("//a[text()=\" seguidores\"]")
        element.click()
        time.sleep(10)
        seguir()
    finally:
        driver.quit()

def deixarDeSeguir():
    try:
        init()
        abrirPerfil("bizudasferias")
        element = driver.find_element_by_xpath("//a[text()=\" seguindo\"]")
        element.click()
        time.sleep(10)
        deixar()
    finally:
        driver.quit()

def ficarDandoLike():
    try:
        init()
        like()
    finally:
        driver.quit()

def init():
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(('name', 'username'))
    )
    login = driver.find_element_by_name('username')
    login.send_keys("bizudasferias@gmail.com")
    senha = driver.find_element_by_name('password')
    senha.send_keys("bizu@ferias@123")
    wait = driver.implicitly_wait(5)
    button = driver.find_element_by_css_selector("button[type=\"submit\"]")
    button.click();
    wait = driver.implicitly_wait(10)
    button = driver.find_element_by_css_selector("button.HoLwm")
    button.click();
    time.sleep(3)


def abrirPerfil(perfil):
    driver.get("https://www.instagram.com/"+perfil+"/")
    time.sleep(5)


def seguir():
    list = driver.find_elements_by_xpath("//button[text()=\"Seguir\"]")
    x = 1
    size = len(list)
    time.sleep(5)
    for el in list:
        el.click()
        time.sleep(random.randint(240, 300))
        if x == size:
            seguir()
        else:
            x = x + 1

def deixar():
    list = driver.find_elements_by_xpath("//button[text()=\"Seguindo\"]")
    x = 1
    size = len(list)
    for elemento in list:
        elemento.click()
        time.sleep(2)
        deixarDeSeguir = driver.find_element_by_xpath("//button[text()=\"Deixar de seguir\"]")
        deixarDeSeguir.click()
        time.sleep(random.randint(240, 300))
        if x == size:
            seguir()
        else:
            x = x + 1

def like():
    list = driver.find_elements_by_css_selector("button > span.glyphsSpriteHeart__outline__24__grey_9");
    x = 1
    size = len(list)
    for elemento in list:
        elemento.click()
        time.sleep(random.randint(25,35))
        if x == size:
            like()
        else:
            x = x + 1

driver = webdriver.Chrome()
