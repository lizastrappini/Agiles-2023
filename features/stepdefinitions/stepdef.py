from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

driver = None
urlJuego = ''
intentos = 5

# Test juego

@given('que el usuario ha ingresado al juego')
def step_impl(context):
    global driver
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/jugar.html')

@when('el usuario juega al juego')
def step_impl(context):
    # No code needed
    pass

@then('la URL del juego debería ser {expectedUrl}')
def step_impl(context, expectedUrl):
    current_url = driver.current_url
    if current_url != expectedUrl:
        raise AssertionError(f"La URL actual es {current_url}, se esperaba {expectedUrl}")
    driver.quit()

# Test inicio

@given('que el usuario ha ingresado a la página principal')
def step_impl(context):
    global driver
    driver = webdriver.Chrome()
    driver.get('')

@when('el usuario navega por la página principal')
def step_impl(context):
    # No code needed
    pass

@then('la URL de la página principal debería ser {expectedUrl}')
def step_impl(context, expectedUrl):
    current_url = driver.current_url
    if current_url != expectedUrl:
        raise AssertionError(f"La URL actual es {current_url}, se esperaba {expectedUrl}")
    driver.quit()

# Test usuario gana partida

@given('el juego comienza con la palabra secreta')
def step_impl(context):
    global driver
    driver = webdriver.Chrome()
    driver.get(urlJuego)

@when('usuario adivina la letra {letter1},{letter2},{letter3},{letter4},{letter5},{letter6}')
def step_impl(context, letter1, letter2, letter3, letter4, letter5,letter6):
    letters = [letter1, letter2, letter3, letter4, letter5, letter6]
    for letter in letters:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, letter))).click()

@then('el usuario recibe mensaje ganaste {word}')
def step_impl(context, word):
    # driver.quit()
    pass

# Test usuario pierde partida

@given('el jugador erra')
def step_impl(context):
    global driver
    global intentos
    letters = ['a', 'r', 'w', 'v', 'q', 'o', 'p', 'b', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    driver = webdriver.Chrome()
    driver.get(urlJuego)

@when('usuario ingresa la letra incorrecta')
def step_impl(context):
    global intentos
    letters = ['a', 'r', 'w', 'v', 'q', 'o', 'p', 'b', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    for letter in letters:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, letter))).click()
        if letter not in "scrum":
            intentos -= 1
        if intentos == 0:
            break

@then('el usuario recibe mensaje perdiste')
def step_impl(context):
    # driver.quit()
    pass
