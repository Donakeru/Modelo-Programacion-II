from abstract_classes.instrumento import Instrumento


class Saxofon(Instrumento):

    def tocar(self):
        if(self.afinado):
            print("El Saxofón está sonanado")
        else:
            print("El Saxofón está sonanado... Desafinado!")