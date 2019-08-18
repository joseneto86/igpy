from Insta import Insta
import sys

class Aplicacao:
    def __init__(self, prefil):
        self.insta = None

    def like(self, cmd):
        self.insta.ficarDandoLike()

    def seguir(self, cmd):
        #instagram.buscarSeguidores(sys.argv[2])
        self.insta.buscarSeguidores()


    def deixar(self, cmd):
        #instagram.deixarDeSeguir()
        self.insta.like()

    def invalid(self, cmd):
        print('[{}] is invalid'.format(cmd))

    def executarAcao(self, cmd):
        switcher = {
            'like': self.like,
            'seguir': self.seguir,
            'deixar': self.deixar
        }
        func = switcher.get(cmd, lambda cmd: self.invalid(cmd))
        return func(cmd)

    def iniciar(self, cmd):
        try:
            self.insta = Insta()
            self.executarAcao(cmd)
        except Exception as e:
            print(e)
        finally:
            self.insta.terminar()
            self.iniciar(cmd)
