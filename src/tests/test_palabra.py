from src.juego import Ahorcado

def test_palabraCorrecta():
    juego = Ahorcado("perro")
    assert juego.verificarPalabra("perro") == True
    
def test_palabraIncorrecta():
    juego = Ahorcado("perro")
    assert juego.verificarPalabra("gato") == False
    
def test_ingresarLetraCorrecta():
    juego = Ahorcado("perro")
    assert juego.verificarLetra("p")== True
    
def test_ingresarLetraCorrecta1():
    juego = Ahorcado("perro")
    assert juego.verificarLetra("e")== True


def test_ingresarLetraIncorrecta():
    juego = Ahorcado("perro")
    assert juego.verificarLetra("g")== False


def test_ingresarLetraIncorrecta2():
    juego = Ahorcado("perro") 
    assert juego.verificarLetra("i")== False
    
def test_contarCantLetras1():
    juego = Ahorcado("perro")
    assert juego.contarLetras() == 5
    
def test_contarCantLetras2():
    juego = Ahorcado("lio")
    assert juego.contarLetras()== 3



def test_iniciar_juego():
    juego = Ahorcado("perro")
    assert juego.intentos_maximos == 5
    assert juego.intentos_restantes == 5
    assert juego.letras_adivinadas == []

def test_intento_exitoso():
    juego = Ahorcado("perro")
    assert juego.intento("p") == True
    assert juego.letras_adivinadas == ["p"]
    assert juego.intentos_restantes == 5

def test_intento_fallido():
    juego = Ahorcado("perro")
    assert juego.intento("z") == False
    assert juego.letras_adivinadas == []
    assert juego.intentos_restantes == 4

def test_estado_del_juego():
    juego = Ahorcado("perro")
    juego.intento("p")
    juego.intento("e")
    assert juego.estado_del_juego() == "pe___"

def test_juego_terminado_ganador():
    juego = Ahorcado("perro")
    juego.intento("p")
    juego.intento("e")
    juego.intento("r")
    juego.intento("r")
    juego.intento("o")

    assert juego.juego_terminado() == True

def test_juego_terminado_perdedor():
    juego = Ahorcado("perro")
    juego.intento("q")
    juego.intento("w")
    juego.intento("e") 
    juego.intento("r")
    juego.intento("z")
    juego.intento("x")
    assert juego.juego_terminado() == False
