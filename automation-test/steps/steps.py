from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    elemento_dificultad =  context.driver.find_element(By.ID, f'{dificultad}')
    #elemento.send_keys(dificultad)
    #context.driver.implicitly_wait(40) 
    elemento_dificultad.click()
    elemento_comenzar =  context.driver.find_element(By.ID, "dificultad").click()

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

    context.driver.implicitly_wait(40) 
    palabra_elemento = context.driver.find_element(By.ID,"palabra_a_adivinar")
    palabra = palabra_elemento.get_attribute("value")
    palabra_guiones = context.driver.find_element(By.ID,"palabra_mostrada").text 
    cantidad_guiones = palabra_guiones.count("_")
    cantidad_letras = len(palabra)

   
    assert cantidad_letras == cantidad_guiones

 

@then('el numero de vidas debe ser 6')
def mantiene_vidas(context):
    intentos_elemento = context.driver.find_element(By.ID,'intentos')
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
    context.driver.implicitly_wait(40) 
    boton_letra = context.driver.find_element(By.ID, f'letra_{letra}')
    
    assert boton_letra.get_attribute("value") == letra
    boton_letra.click()
    
    
@then('El jugador pierde una vida')
def pierde_vida(context):
    intentos_elemento = context.driver.find_element(By.ID,'intentos')
    intentos = intentos_elemento.get_attribute("value")

    assert int(intentos) < 6


@then('Se muestra como letra usada "{letra}"')
def estado_letra(context, letra):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, f'letra_{letra}'))
    )
    letra_elemento = context.driver.find_element(By.ID, f'letra_{letra}')
    assert not letra_elemento.is_enabled()
    
# ingresa letra correcta

@then('La palabra contiene la "{letra}"')
def estado_palabra_adivinar(context,letra):
    context.driver.implicitly_wait(10) 
    texto_elemento = context.driver.find_element(By.ID,'palabra_a_adivinar') 
    palabra_a_adivinar = texto_elemento.get_attribute("value")
    assert letra in palabra_a_adivinar


# Reiniciar el juego
@given('El jugador selecciona una letra')
def ingresa_letra(context):
    context.driver.get(HOME_URL)
    WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.ID, 'letra')))
    
    element= context.driver.find_element(By.ID,'letra')
    element.click()
    
 
   
    
@when('El jugador reinicia el juego')
def reinicia(context):
    context.driver.find_element(By.ID,"botonVolver").click()


def after_scenario(context, scenario):
    context.driver.quit()


@given('El jugador selecciona la letra "{letra}"')
def ingresa_letra(context,letra):
    context.driver.implicitly_wait(40) 
    boton_letra = context.driver.find_element(By.ID, f'letra_{letra}')
    assert boton_letra.get_attribute("value") == letra
    boton_letra.click()