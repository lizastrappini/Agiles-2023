import random


# Palabras disponibles
palabras_facil = [["sal", "Fuente principal de luz del sistema solar"], ["gato", "Animal doméstico de compañía"],["casa", "Lugar donde vives"] ]
palabras_intermedio = [["travesia", "Largo viaje o trampolín de experiencias"],["aventura", "Viaje emocionante y arriesgado"], ["melodia", "Secuencia armoniosa de sonidos"] ]
palabras_dificil = [["efimero", "Que dura por un corto periodo de tiempo"],["magico", "Relacionado con la magia o algo extraordinario"], ["enigma", "Misterio o situación difícil de entender"]]


# Crea una lista de letras del abecedario
abecedario =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

class Ahorcado():
    def __init__(self):
        self.intentos = 6
        self.letras_adivinadas = []
        self.fin_juego = False
        self.letras_usadas = []
        self.palabra_mostrada = ''
        self.pista = ''
        self.dificultad = ''
        self.palabra_a_adivinar = ['','']
        self.intentos_restantes = 6


    def iniciar(self, dificultad=None, palabra=None):
        self.intentos = 6
        self.letras_adivinadas = []
        self.fin_juego = False
        self.letras_usadas = []
        if palabra is None:
            self.palabra_a_adivinar = self.elegir_palabra(dificultad)
            self.palabra_mostrada = self.crear_lineas(self.palabra_a_adivinar[0])
        else:
            self.palabra_a_adivinar[0] = palabra
            self.palabra_mostrada = self.crear_lineas(palabra)
        self.pista = ''
        self.dificultad = dificultad
        self.intentos_restantes = 6


    def elegir_palabra(self,dificultad):
        if dificultad == 'facil':
            return random.choice(palabras_facil)
        elif dificultad == 'media':
            return random.choice(palabras_intermedio)
        else:
            return random.choice(palabras_dificil)

    # Obtengo la pista asociada a la palabra a adivinar
    def obtener_pista(self):
        self.pista = self.palabra_a_adivinar[1]
        return self.pista
    
    # Verificar si las letras usadas estan en la palabra a adivinar
    def revelar_letra(self,letra):
        letras_adiv =''
        for l in self.palabra_a_adivinar[0]:
            if l ==letra or l in self.letras_usadas:
                letras_adiv+=l
            else:   
                letras_adiv+='_'
        self.palabra_mostrada = letras_adiv  
    
    # Decrementar intentos
    def decrementar_intentos(self):
        self.intentos -= 1
        self.intentos_restantes = self.intentos 

    def contar_letras(self, palabra):
        return len(palabra)
    
    # Creo las lineas de la palabra a adivinar
    # Si la letra no esta en la palabra muestra un guion bajo, sino muestra la letra
    def crear_lineas(self, palabra):
        self.palabra_mostrada = '_' * self.contar_letras(palabra)
        return self.palabra_mostrada

    def intento(self,letra):
        print(letra)
        if( self.verificar_letra(letra) ):
            self.revelar_letra(letra)
            print(self.palabra_mostrada)
            return True
        else:
            self.decrementar_intentos()
            return False
    
    # Verifica si la letra ingresada esta en la palabra a adivinar
    def verificar_letra(self, letra):
        if letra in self.palabra_a_adivinar[0]:
            self.letras_usadas += letra	
            self.letras_adivinadas += letra	
            return True
        else:
            return False
    

    def verificar_palabra(self, palabra):
        if palabra == self.palabra_a_adivinar[0]:
            return True
        else:
            return False

        
    # Verifica si la letra ingresada ya fue usada
    def letraUsada(self, letra):
        if letra in self.letras_adivinadas:
            return True
        else:
            return False
    
    # Verificar si termino el juego
    def verificar_fin_juego(self):
        if self.intentos == 0 or (self.palabra_mostrada == self.palabra_a_adivinar[0]):
            self.fin_juego = True
        return self.fin_juego

    
    def abecedario(self):
        return abecedario