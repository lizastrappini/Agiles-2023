Feature: Juego del Ahorcado

  Scenario: Iniciar nuevo juego
      Given Ingreso a la pagina del juego
      When Elige "<dificultad>" y hace click en comenzar
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6

  Scenario: Ingresar una letra incorrecta
      Given El jugador inicia el juego
      When El jugador selecciona una letra 
      Then El jugador pierde una vida
   

  Scenario: Adivinar una letra correcta
      Given El jugador inicia el juego
      When El jugador selecciona una letra 
      Then La palabra contiene la "<letra>"
      And el numero de vidas debe ser 6
 
 
  Scenario: Reinicia el juego
      Given El jugador inicia el juego
      And El jugador selecciona una letra 
      When El jugador reinicia el juego
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6
    
