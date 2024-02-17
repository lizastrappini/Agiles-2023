from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


HOME_URL = "https://ahorcado-metod-agiles.onrender.com/"

  
# Iniciar nuevo juego
@given('Ingreso a la pagina del juego')
def abrir_pagina(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(HOME_URL)
    
@when('Elige "{dificultad}" y hace click en comenzar')
def comienza_juego(context, dificultad):

    elemento_dificultad =  WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, f'{dificultad}'))
    )
    elemento_dificultad.click()
    elemento_comenzar =  WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.NAME, "comenzar"))
    )
    elemento_comenzar.click()



@then('la palabra a adivinar debe mostrarse con guiones')
def palabra_guiones(context):

    palabra_elemento = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID,"palabra_a_adivinar"))
        )
    palabra = palabra_elemento.get_attribute("value")
    palabra_guiones = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID,"palabra_mostrada"))
    )
    palabra_guiones_texto = palabra_guiones.text
    cantidad_guiones = palabra_guiones_texto.count("_")
    cantidad_letras = len(palabra)

    assert cantidad_letras == cantidad_guiones

 

@then('el numero de vidas debe ser 6')
def mantiene_vidas(context):
    intentos_elemento = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID,'intentos'))
    )
    intentos = intentos_elemento.get_attribute("value")

    assert int(intentos) == 6

# ingresa letra incorrecta
@given('El jugador inicia el juego')
def empieza_juego(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=options)
    context.driver.get(HOME_URL)

    
@when('El jugador selecciona la letra "{letra}"')
def ingresa_letra(context,letra):

    boton_letra = WebDriverWait(context.driver,30 ).until(
        EC.presence_of_element_located((By.ID, f'letra_{letra}'))
    )    
    assert boton_letra.get_attribute("value") == letra
    boton_letra.click()
    
    
@then('El jugador pierde una vida')
def pierde_vida(context):
    intentos_elemento = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID,'intentos'))
    )
    intentos = intentos_elemento.get_attribute("value")

    assert int(intentos) < 6


@then('Se muestra como letra usada "{letra}"')
def estado_letra(context, letra):
    letra_elemento = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, f'letra_{letra}'))
    )
    assert not letra_elemento.is_enabled()
    
# ingresa letra correcta

@then('La palabra contiene la "{letra}"')
def estado_palabra_adivinar(context,letra):

    texto_elemento = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID,'palabra_a_adivinar'))
    )
    palabra_a_adivinar = texto_elemento.get_attribute("value")
    assert letra in palabra_a_adivinar


# Reiniciar el juego
@given('El jugador selecciona una letra')
def ingresa_letra(context):
    context.driver.get(HOME_URL)
    letra_elemento = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'letra'))
    )
    letra_elemento.click()
    
 
   
    
@when('El jugador reinicia el juego')
def reinicia(context):
    boton_volver = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID,"botonVolver"))
    )
    boton_volver.click()

def after_scenario(context, scenario):
    context.driver.quit()


@given('El jugador selecciona la letra "{letra}"')
def ingresa_letra(context,letra):
    context.driver.implicitly_wait(40) 
    boton_letra = WebDriverWait(context.driver, 30).until(
        EC.presence_of_element_located((By.ID, f'letra_{letra}'))
    
    )
    assert boton_letra.get_attribute("value") == letra
    boton_letra.click()