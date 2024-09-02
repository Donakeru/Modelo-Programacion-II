from abc import ABC, abstractmethod

class Instrumento(ABC):
    
    def __init__(self):
        self.afinado = False
    
    def afinar(self):
        self.afinado = True
        print("El instrumento está afinado")
    
    @abstractmethod
    def tocar(self):
        """
            Para cada clase concreta derivada de esta clase
            se debe hacer una implementación de este método
        """
        pass