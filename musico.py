class Musico:
    
    def __init__(self, nombre, instrumento_asignado):
        self.nombre = nombre
        self.instrumento_asignado = instrumento_asignado
    
    def revisar_afinacion(self):
        return self.instrumento_asignado.afinado
    
    def afinar_instrumento(self):
        self.instrumento_asignado.afinar()
        
    def tocar_instrumento(self):
        self.instrumento_asignado.tocar()