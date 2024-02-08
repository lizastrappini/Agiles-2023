Feature: Juego del Ahorcado

  Scenario: Iniciar nuevo juego
      Given Ingreso a la pagina del juego
      When Elige la dificultad e inicia el juego
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6

  Scenario: Ingresar una letra incorrecta
      Given El jugador inicia el juego
      When El jugador ingresa la letra "<letra>"
      Then El jugador pierde una vida
      And Se resalta como letra incorrecta "<letra>"

  Scenario: Adivinar una letra correcta
      Given El jugador inicia el juego
      When El jugador ingresa la letra "<letra>"
      Then La palabra contiene la "<letra>"
      And el numero de vidas debe ser 6
 
 
  Scenario: Reinicia el juego
      Given El jugador inicia el juego
      And El jugador ingresa la letra "<letra>"
      When El jugador reinicia el juego
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6
    
