from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import instagram
import sys


def like(cmd):
    instagram.ficarDandoLike()


def seguir(cmd):
    if len(sys.argv) > 2:
        instagram.buscarSeguidores(sys.argv[2])
    else:
        print("digite um perfil pra seguir")


def deixar(cmd):
    instagram.deixarDeSeguir()

def invalid(cmd):
    print('[{}] is invalid'.format(cmd))

def invoke_command(cmd):
    switcher = {
        'like': like,
        'seguir': seguir,
        'deixar': deixar
    }
    func = switcher.get(cmd, lambda cmd: invalid(cmd))
    return func(cmd)


_opcao_ = ""
if len(sys.argv)> 1:
   _opcao_ = sys.argv[1]
   cmd = sys.argv[1]
   invoke_command(cmd)

else:
    print("opcao invalida")

