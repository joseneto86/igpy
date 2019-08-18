import sys
from Aplicacao import Aplicacao

_opcao_ = ""
if len(sys.argv)> 1:
   _opcao_ = sys.argv[1]
   perfil = None
   if( len(sys.argv)>2):
       perfil = sys.argv[2]
   app = Aplicacao(perfil)
   app.iniciar(_opcao_)
else:
    print("opcao invalida")

