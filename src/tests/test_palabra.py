from Main import Ahorcado


def test_palabraCorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ['perro', '']
    assert juego.verificar_palabra('perro') == True
    
def test_palabraIncorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ['perro', '']
    assert juego.verificar_palabra("gato") == False


def test_ingresarLetraCorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ['perro', '']
    letras_usadas = []
    letra = 'p'
    assert juego.verificar_letra(letra)== True
    
def test_ingresarLetraCorrecta1():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ['perro', '']
    letras_usadas = []
    letra = 'o'
    assert juego.verificar_letra(letra)== True


def test_ingresarLetraIncorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ['perro', '']
    letras_usadas = []
    letra = 'x'
    assert juego.verificar_letra(letra)== False


def test_ingresarLetraIncorrecta2():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ['perro', '']
    letras_usadas = []
    letra = 'n'
    assert juego.verificar_letra(letra)== False

 
def test_contarCantLetras1():
    juego = Ahorcado()
    assert juego.contar_letras('perro') == 5
    
def test_contarCantLetras2():
    juego = Ahorcado()
    assert juego.contar_letras('lio')== 3



def test_iniciar_juego():
    juego = Ahorcado()
    assert juego.intentos == 6
    assert juego.intentos_restantes == 6
    assert juego.letras_adivinadas == []

def test_intento_exitoso():
    juego = Ahorcado()
    juego.palabra_a_adivinar = 'perro'
    assert juego.intento("p") == True
    assert juego.letras_adivinadas == ['p']
    assert juego.intentos_restantes == 6

def test_intento_fallido():
    juego = Ahorcado()
    juego.palabra_a_adivinar = 'perro'
    assert juego.intento('z') == False
    assert juego.letras_adivinadas == []
    assert juego.intentos_restantes == 5

def test_estado_del_juego():
    juego = Ahorcado()
    juego.iniciar()
    juego.intento('p')
    juego.intento('e')
    assert juego.verificar_fin_juego() == False

def test_juego_terminado_ganador():
    juego = Ahorcado()
    juego.iniciar(palabra='gato')
    juego.intento('g')
    juego.intento('a')
    juego.intento('t')
    juego.intento('o')
    assert juego.verificar_fin_juego() == True

def test_juego_terminado_perdedor():
    juego = Ahorcado()
    juego.iniciar(palabra='perro')
    juego.intento("q")
    juego.intento("w")
    juego.intento("y") 
    juego.intento("m")
    juego.intento("z")
    juego.intento("x")
    assert juego.verificar_fin_juego() == True
