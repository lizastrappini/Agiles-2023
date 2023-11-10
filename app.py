from flask import Flask, render_template, request, redirect, url_for, session
import random
from ahorcado import Ahorcado

app = Flask(__name__)
app.secret_key = 'esto-es-una-clave-muy-secreta'
# Lista de palabras para el juego
palabras = ["python", "flask", "javascript", "html", "css", "git", "sql", "mongodb"]
a = Ahorcado()
# Función para obtener una palabra aleatoria de la lista
def obtener_palabra():
    return random.choice(palabras)

# Ruta principal del juego
@app.route('/')
def index():
    session.clear()
    a.limpiar_variables_total
    session["ing"] = request.form.get('ingreso')
    
    if session["ing"].upper() == session["palabra"]:
            session["puntaje"] = a.dev_puntaje(8)
            a.limpiar_variables_parcial()
    else:
            print(session["intentos"])
            session["intentos"] = 0
            session["puntaje"] = a.dev_puntaje(0)
    
    a.ingresa_letra(session["ing"].upper())
    if session["palabra"] == session["guia"]:
        session["puntaje"] = a.dev_puntaje(session["intentos"]) 
        a.limpiar_variables_parcial()
    return render_template('play.html', puntaje = session["puntaje"], letra = session["ing"], dificultad=session["dificultad"],alias=session["user"], intentos =session["intentos"], palabra = session["palabra"], largo = session["largo"], guia = session["guia"], leting = session["letrasing"])

    

if __name__ == '__main__':
    app.secret_key = 'clave_secreta'
    app.run(debug=True)
