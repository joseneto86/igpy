from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys

class Insta:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.concorrentes = ["rnatural", "viajandoeusoufeliz", "viajandocomgabi", "malasemalinhas", "eunonordeste", "viajandinhas", "suaproximaviagem"]
    def ficarDandoLike(self):
        self.init()
        self.like()
    def buscarSeguidores(self):
        self.init()
        num = random.randint(0, len(self.concorrentes))
        self.seguir(self.concorrentes[num])

    def init(self):
        actions = ActionChains(self.driver)
        self.driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(('name', 'username'))
        )
        login = self.driver.find_element_by_name('username')
        login.send_keys("bizudasferias@gmail.com")
        senha = self.driver.find_element_by_name('password')
        senha.send_keys("bizu@ferias@123")
        wait = self.driver.implicitly_wait(5)
        button = self.driver.find_element_by_css_selector("button[type=\"submit\"]")
        button.click();
        wait = self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_css_selector("button.HoLwm")
        button.click();
        time.sleep(3)

    def abrirPerfil(self, perfil):
        self.driver.get("https://www.instagram.com/"+perfil+"/")
        time.sleep(5)
    

    def seguir(self, perfil):
        self.abrirPerfil(perfil)
        element = self.driver.find_element_by_xpath("//a[text()=\" seguidores\"]")
        element.click()
        time.sleep(5)
        list = self.driver.find_elements_by_css_selector("div.HVWg4")
        top = 350
        x = 0
        for el in list:
            botao = el.find_element_by_css_selector("button.L3NKy")
            x = x + 1
            if( x % 8 == 0 and x > 1 ):
                #self.driver.execute_script("document.querySelector('div.isgrP').scrollTop="+str(top))
                top = 350 + top
            if( botao.get_attribute('innerHTML')=="Seguir"):
                link = el.find_element_by_css_selector("a.FPmhX")
                href = link.get_attribute('href')
                self.driver.get(href)
                self.acaoPaginaInstagramSeguir()
                break
            else:
                continue
        time.sleep(random.randint(200,300))
        self.seguir(perfil)


    def like(self):
        list = self.driver.find_elements_by_css_selector("button > span.glyphsSpriteHeart__outline__24__grey_9");
        x = 1
        size = len(list)
        for elemento in list:
            elemento.click()
            time.sleep(random.randint(25,35))
            if x == size:
                self.like()
            else:
                x = x + 1
    def terminar(self):
        self.driver.quit()

    def clicarImgSeguidor(self, listaImg, index):
        img = listaImg[index]
        img.click()
        pic = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.KL4Bh img"))
        )
        botao =  self.driver.find_element_by_css_selector("button > span.glyphsSpriteHeart__outline__24__grey_9")
        time.sleep(5)
        botao.click()
        time.sleep(2)
        fechar = self.driver.find_element_by_css_selector("button.ckWGn")
        fechar.click()
        time.sleep(2)

    def acaoPaginaInstagramSeguir(self):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()=\"Seguir\"]"))
        )
        try:
            privado = self.driver.find_element_by_css_selector('h2.rkEop')
        except:
            listaImg = self.driver.find_elements_by_css_selector("div._bz0w a")
            if( len(listaImg) > 3):
                self.clicarImgSeguidor(listaImg, 0)
                indexPic1 = random.randint(1,len(listaImg))
                self.clicarImgSeguidor(listaImg, indexPic1)
                indexPic2 = random.randint(1,len(listaImg))
                while indexPic1 == indexPic2:
                    indexPic2 = random.randint(1,len(listaImg))
                self.clicarImgSeguidor(listaImg, indexPic2)
            else:
                x = 0
                for img in listaImg:
                    self.clicarImgSeguidor(listaImg,x)
                    x = x + 1
        finally:
            seguir = self.driver.find_element_by_xpath( "//button[text()=\"Seguir\"]" )
            seguir.click()



