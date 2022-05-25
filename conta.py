

class Conta:
    def __init__(self, numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    # Getters (pegar uma informação) and Setters (alterar uma informação)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
