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
    
    def generar_chisga(self):
        
        cantidad_musicos = random.randint(1,self.max_musicos)
        print(f'Cantidad de músicos por generar: {cantidad_musicos}',)        
        for i in range(1, cantidad_musicos+1):
            instrumento = self.obtener_instancia(random.choice(self.listaInstrumentos))
            self.listaMusicos.append(Musico(nombre= f'Musico #{i}' ,instrumento_asignado=instrumento))
            
    def ver_integrantes(self):
        if(len(self.listaMusicos) == 0):
            print("NOTA: Por favor genere primero una chisga")
        else:
            print('-'*3, 'Alineación','-'*3)
            for musico in self.listaMusicos:
                print(f'{musico.nombre} tiene como instruemnto: {musico.instrumento_asignado.__class__.__name__}')
        
    def afinar_chisga(self):
    
        if(len(self.listaMusicos) == 0):
            print("Por favor genere primero una chisga")
        else:
            print('-'*3, 'Afinación','-'*3)
            if(self.musicos_afinados == False):
                for musico in self.listaMusicos:
                    if (musico.revisar_afinacion() == False):
                        musico.afinar_instrumento()
                self.musicos_afinados = True
                print("¡Instrumentos afinados!")
            else:
                print("Los instrumentos ya está afinados")
                
    def empezar_funcion(self):
        if(len(self.listaMusicos) == 0):
            print("Por favor genere primero una chisga")
        else:
            if(self.musicos_afinados == False):
                print("Los músicos no han afinado ¡No pueden empezar!")
            else:
                
                print(
                    """
                    +----------------------------+
                    |   La función va a empezar  |
                    +----------------------------+
                    1...2...1...2...3...4
                    """
                )
                
                for musico in self.listaMusicos:
                    print(f'{musico.nombre}: ')
                    musico.tocar_instrumento()
                    