from abstract_classes.instrumento import Instrumento


class Guitarra(Instrumento):

    def tocar(self):
        if(self.afinado):
            print("La Guitarra está sonanado")
        else:
            print("La Guitarra está sonanado... Desafinada!")