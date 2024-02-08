from flask import Flask, render_template, request
from Main import Ahorcado


app = Flask(__name__)


juego = Ahorcado()

# Clave para poder utilizar variables de sesion
app.secret_key = 'tu_clave_secreta'

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/empezar',methods=['POST'])
def empezar():
    dificultad = request.form.get('dificultad')
    juego.iniciar(dificultad)
    print(juego.palabra_a_adivinar)
    print(juego.palabra_mostrada)
    return render_template('jugar.html',dificultad=juego.dificultad, pista=juego.pista, palabra_a_adivinar=juego.palabra_a_adivinar[0], abecedario=juego.abecedario(), intentos=juego.intentos, letras_adivinadas=juego.letras_adivinadas, palabra_mostrada=juego.palabra_mostrada, letras_usadas=juego.letras_usadas, fin_juego=juego.fin_juego)


@app.route('/jugar', methods=['POST'])
def jugar():

    # Recupero las letras usadas 
    letras_usadas = juego.letras_usadas


    # Recupero la palabra a adivinar 
    palabra = juego.palabra_a_adivinar[0]


    # Recupero la letra segun el boton que se presiono
    letra = request.form.get('letra').lower()

    
    # Agrego la letra a la lista de letras usadas
    letras_usadas.append(letra)


    # Actualizo la variable con la lista de letras usadas para no poder seguir utilizandola en los siguientes intentos
    juego.letras_usadas = letras_usadas

    # Si la letra esta en la palabra la revelo, si no decremento intentos
    juego.intento(letra)

    # Si no quedan mas intentos o si la palabra fue adivinada termina el juego
    juego.verificar_fin_juego()


    
    return render_template('jugar.html', dificultad=juego.dificultad, pista=juego.pista, palabra_mostrada=juego.palabra_mostrada, letras_adivinadas=juego.letras_adivinadas, intentos=juego.intentos, abecedario=juego.abecedario(), letras_usadas=juego.letras_usadas,palabra_a_adivinar=juego.palabra_a_adivinar[0], fin_juego=juego.fin_juego) 

    
@app.route('/pista', methods=['POST'])
def pista():
    juego.obtener_pista()
    return render_template('jugar.html', dificultad=juego.dificultad, pista=juego.pista, palabra_mostrada=juego.palabra_mostrada, letras_adivinadas=juego.letras_adivinadas, intentos=juego.intentos,abecedario=juego.abecedario(), letras_usadas=juego.letras_usadas,palabra_a_adivinar=juego.palabra_a_adivinar[0],fin_juego=juego.fin_juego)


if __name__ == '__main__':
    app.run(debug=True)
