Feature: Juego del Ahorcado

  Scenario: Iniciar nuevo juego
      Given Ingreso a la pagina del juego
      When Elige la dificultad e inicia el juego
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6
 

  Scenario : Adivinar una letra correcta
      Given El jugador inicia el juego
      When El jugador ingresa la letra "<letra>"
      Then La palabra contiene la "<letra>"
      And el numero de vidas debe ser 6
    

  Scenario : Ingresar una letra incorrecta
      Given El jugador inicia el juego
      When El jugador ingresa la letra "<letra>"
      Then El jugadir pierde una vida
      And Se resalta como letra incorrecta "<letra>"

 
  Scenario: Pierde el juego
    Given El jugador inicia el juego
    When El jugador ingresa 6 caracteres incorrectos
    Then El jugador pierde el juego
    Then Muestra el mensaje de que perdio con la palabra a adivinar

     
  Scenario: Gana el juego
    Given El jugador inicia el juego
    When El jugador ingresa los caracteres correctos
    Then El jugador gana el juego
    Then Muestra el mensaje de que gano con la palabra adivinada
  
  Scenario: Reinicia el juego
    Given El jugador inicia el juego
    And El jugador ingresa la letra "<letra>"
    When El jugador reinicia el juego
    Then la palabra a adivinar debe mostrarse con guiones
    And el numero de vidas debe ser 6
    

  Scenario: Vuelve al inicio
    Given El jugador inicia el juego
    And El jugador ingresa la letra "<letra>"
    When El jugador vuelve al inicio el juego
    Then las dificultades del juego se muestran en pantalla
    Then la palabra a adivinar debe mostrarse con guiones
    And el numero de vidas debe ser 6
   