from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

HOME_URL = "https://ahorcado-metod-agiles.onrender.com/"

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
def after_scenario(context, scenario):
    context.driver.quit()
    

# @when('Elige la dificultad e inicia el juego')
# def comienza_juego(context):
#     context.driver.get(HOME_URL)

@when('Elige la dificultad e inicia el juego')
def comienza_juego(context, opcion):
    dropdown = esperar_elemento(context, By.ID, "opcion")
    select = Select(dropdown)
    select.select_by_visible_text(opcion)


@then('la palabra a adivinar debe mostrarse con guiones')
def palabra_con_guiones(context):
    texto = context.driver.find_element(By.ID,'palabraAhorcado').text  
    assert '_' in texto

@then('el numero de vidas debe ser 6')
def mantiene_vidas(context):
    h2 = context.driver.find_element(By.ID,'vidas').text
    digitos = int(''.join(caracter for caracter in h2 if caracter.isdigit()))
    assert digitos == 6

# ingresa letra incorrecta
@given('El jugador inicia el juego')
def comienza_juego(context):
    context.driver.get(HOME_URL)
    
@when('El jugador ingresa la letra "{letra}"')
def ingresa_letra(context,letra):
    elemento =  context.driver.find_element(By.NAME,"input")
    elemento.send_keys(letra)
    context.driver.implicitly_wait(40) 

    context.driver.find_element(By.NAME,"adivinar").click()
    
    
@then('El jugador pierde una vida')
def pierde_vida(context):
    h2 = context.driver.find_element(By.ID,'vidas').text
    vidas = int(''.join(caracter for caracter in h2 if caracter.isdigit()))

    assert vidas < 6



@then('Se resalta como letra incorrecta "{letra}"')
def letras_incorrectas(context,letra):
    texto = context.driver.find_element(By.ID,'incorrectas').text  
    incorrectas = eval(texto)
    assert letra in incorrectas
    
# ingresa letra correcta

@then('La palabra contiene la "{letra}"')
def estado_palabra_adivinar(context,letra):
    texto = context.driver.find_element(By.ID,'palabraAhorcado').text  
    palabra_adivinar = eval(texto)
    assert letra in palabra_adivinar


# Reiniciar el juego
@given('El jugador ingresa la letra "{letra}"')
def ingresa_letra(context,letra):
    elemento =  context.driver.find_element(By.NAME,"input")
    elemento.send_keys(letra)
    context.driver.implicitly_wait(40) # seconds

    context.driver.find_element(By.NAME,"adivinar").click()
    
    
@when('El jugador reinicia el juego')
def reinicia(context):
    context.driver.find_element(By.NAME,"reinicia").click()


