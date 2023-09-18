palabra= "perro"

def verificarPalabra(string):
    if(string=="perro"):
        return True
    else: return False
    
def verificarLetra(letra):
    if(letra in palabra ):
        return True
    else: return False
    
def contarLetras(palabraIngresada):
    return len(palabraIngresada)