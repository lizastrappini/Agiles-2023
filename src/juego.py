
class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.intentos_maximos = 5
        self.intentos_restantes = self.intentos_maximos
        self.letras_adivinadas = []

    def intento(self, letra):
        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
            return True
        else:
            self.intentos_restantes -= 1
            return False

    def estado_del_juego(self):
        estado = ""
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                estado += letra
            else:
                estado += "_"
        return estado

    def juego_terminado(self):
        if "_" not in self.estado_del_juego() or self.intentos_restantes <= 0:
            return True
        return False

    
    def verificarPalabra(self,string):
         if(string==self.palabra):
             return True
         else: return False
    
    def verificarLetra(self,letra):
            if(letra in self.palabra ):
                return True
            else: return False
    
    def contarLetras(self):
        return len(self.palabra)

