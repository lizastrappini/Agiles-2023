from behave import *

urlJuego = ""


# Partida Ganada
@given('el juego comienza con la palabra secreta')
def step_impl(context):
    context.browser.get(urlJuego)

@when('usuario adivina la letra {string},{string},{string},{string},{string},{string}')
def step_impl(context):
    assert True is not False

@then('el usuario recibe mensaje ganaste "Felicitaciones! Haz ganado.."')
def step_impl(context):
    assert context.failed is False
    
    
# Partida Perdida
@given('el jugador erra')
def step_impl(context):
    pass

@when('usuario ingresa la letra incorrecta')
def step_impl(context):
    assert True is not False

@then('el usuario recibe mensaje perdiste')
def step_impl(context):
    assert context.failed is False