from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

HOME_URL = "https://ahorcado-metod-agiles.onrender.com/"


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)

def esperar_elemento(context, by, value):
    return WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((by, value))
    )
    
# Iniciar nuevo juego
@given('Ingreso a la pagina del juego')
def abrir_pagina(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(HOME_URL)
    
@when('Elige "{dificultad}" y hace click en comenzar')
def comienza_juego(context, dificultad):
    elemento =  context.driver.find_element(By.NAME,"dificultad")
    elemento.send_keys(dificultad)
    context.driver.implicitly_wait(40) 
    context.driver.find_element(By.NAME,"comenzar").click()
    # dropdown = esperar_elemento(context, By.ID, 'seleccion')
    # context.driver.implicitly_wait(40) 
    # select = Select(dropdown)
    # select.select_by_visible_text(dificultad)

# @when('El juegador hace click en Empezar')
# def inicio(context):
#     boton = esperar_elemento(context, By.XPATH, "//button[contains(text(), 'Empezar')]")
#     boton.click()


@then('la palabra a adivinar debe mostrarse con guiones')
def palabra_guiones(context):
    texto = context.driver.find_element(By.ID,'palabraAhorcado').text  
    inicio_lista = texto.find("_")

    palabra_guiones = eval(texto[inicio_lista:])

    print(palabra_guiones)
    print(palabra_guiones.count('_'))
    print(len(palabra_guiones))
    
    assert palabra_guiones.count('_') == len(palabra_guiones)


@then('el numero de vidas debe ser 6')
def mantiene_vidas(context):
    h2 = context.driver.find_element(By.ID,'vidas').text
    print(h2)
    digitos = int(''.join(caracter for caracter in h2 if caracter.isdigit()))
    print(digitos)
    assert digitos == 6

# ingresa letra incorrecta
@given('El jugador inicia el juego')
def empieza_juego(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)

    context.driver.get(HOME_URL)
    
@when('El jugador selecciona una letra')
def ingresa_letra(context):
    context.driver.get(HOME_URL)
    WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.ID, 'letra')))
    
    # context.driver.implicitly_wait(40) # seconds
    
    element= context.driver.find_element(By.ID,'letra')
    element.click()
    
    
 
    
    
    
@then('El jugador pierde una vida')
def pierde_vida(context):
    h2 = context.driver.find_element(By.ID,'intentos').text
    print(h2)
    vidas = int(''.join(caracter for caracter in h2 if caracter.isdigit()))

    assert vidas < 6

    
# ingresa letra correcta

@then('La palabra contiene la "{letra}"')
def estado_palabra_adivinar(context,letra):
    texto = context.driver.find_element(By.ID,'palabra').text  
    palabra_adivinar = eval(texto)
    assert letra in palabra_adivinar


# Reiniciar el juego
@given('El jugador selecciona una letra')
def ingresa_letra(context):
    context.driver.get(HOME_URL)
    WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.ID, 'letra')))
    
    # context.driver.implicitly_wait(40) # seconds
    
    element= context.driver.find_element(By.ID,'letra')
    element.click()
    
 
   
    
@when('El jugador reinicia el juego')
def reinicia(context):
    context.driver.find_element(By.ID,"reset").click()


def after_scenario(context, scenario):
    context.driver.quit()