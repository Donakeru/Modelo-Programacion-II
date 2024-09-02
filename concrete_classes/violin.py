from abstract_classes.instrumento import Instrumento


class Violin(Instrumento):
    
    def tocar(self):
        if(self.afinado):
            print("El Violín está sonanado")
        else:
            print("El Violín está sonanado... Desafinado!")