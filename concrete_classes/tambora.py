from abstract_classes.instrumento import Instrumento


class Tambora(Instrumento):
    
    def tocar(self):
        if(self.afinado):
            print("La Tambora está sonanado")
        else:
            print("La Tambora está sonanado... Desafinada!")