import random

from concrete_classes.guitarra import Guitarra
from concrete_classes.saxofon import Saxofon
from concrete_classes.tambora import Tambora
from concrete_classes.violin import Violin
from musico import Musico

class Chisga:
    
    def __init__(self):
        self.max_musicos = 10
        self.musicos_afinados = False
        self.listaMusicos = []
        self.listaInstrumentos = ['Guitarra', 'Violin', 'Saxofon', 'Tambora']
    
    def obtener_instancia(self, nombre_instrumento):
        if (nombre_instrumento == 'Guitarra'):
            return Guitarra()
        elif (nombre_instrumento == 'Violin'):
            return Violin()
        elif (nombre_instrumento == 'Saxofon'):
            return Saxofon()
        elif (nombre_instrumento == 'Tambora'):
            return Tambora()
    
    def generarChisga(self):
        cantidad_musicos = random.randint(1,self.max_musicos)
        print(cantidad_musicos)
        print('--'*5)
        for i in range(1, cantidad_musicos+1):
            instrumento = self.obtener_instancia(random.choice(self.listaInstrumentos))
            self.listaMusicos.append(Musico(nombre= f'Musico #{i}' ,instrumento_asignado=instrumento))
        print(self.listaMusicos)
        
    def afinarChisga(self):
    
        if(len(self.listaMusicos) == 0):
            print("Por favor genere primero una chisga")
        else:
            if(self.musicos_afinados == False):
                for musico in self.listaMusicos:
                    if (musico.revisar_afinacion() == False):
                        musico.afinar_instrumento()
                self.musicos_afinados = True
                print("¡Instrumentos afinados!")
            else:
                print("Los instrumentos ya está afinados")
                
    def empezarFuncion(self):
        if(self.musicos_afinados == False):
            print("Los músicos no han afinado ¡No pueden empezar!")
            