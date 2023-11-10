Feature: Verificar que el usuario haya ganado la partida

  Scenario: usuario gana la partida
    Given el juego comienza con la palabra secreta
    When usuario adivina la letra "p","y","t","h","o", "n"
    Then el usuario recibe mensaje ganaste "Felicitaciones! Haz ganado.."

