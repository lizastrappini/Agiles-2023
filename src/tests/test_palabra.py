from src.juego import verificarPalabra, verificarLetra, contarLetras

def test_palabraCorrecta():
    assert verificarPalabra("perro") == True
    
def test_palabraIncorrecta():
    assert verificarPalabra("gato") == False
    
def test_ingresarLetraCorrecta():
    assert verificarLetra("p")== True
    
def test_ingresarLetraCorrecta1():
    assert verificarLetra("e")== True


def test_ingresarLetraIncorrecta():
    assert verificarLetra("g")== False


def test_ingresarLetraIncorrecta2():
    assert verificarLetra("i")== False
    
def test_contarCantLetras1():
    assert contarLetras("perro") == 5
    
def test_contarCantLetras2():
    assert contarLetras("lio")== 6



