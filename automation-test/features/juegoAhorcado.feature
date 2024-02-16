Feature: Juego del Ahorcado

  Scenario Outline: Iniciar nuevo juego
      Given Ingreso a la pagina del juego
      When Elige "<dificultad>" y hace click en comenzar
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6

    Examples: 
        | dificultad |                       
        | facil |
        | media |
        | dificil |

  Scenario Outline: Ingresar una letra incorrecta
      Given El jugador inicia el juego
      When Elige "<dificultad>" y hace click en comenzar 
      And El jugador selecciona la letra "<letra>"
      Then El jugador pierde una vida
      And Se muestra como letra usada "<letra>"

    Examples: 
        | dificultad    |   letra   |                   
        | facil         |     x     |
        | media         |     w     |
        | dificil       |     z     |


  Scenario Outline: Adivinar una letra correcta
      Given El jugador inicia el juego
      When Elige "<dificultad>" y hace click en comenzar 
      And El jugador selecciona la letra "<letra>"
      Then La palabra contiene la "<letra>"
      And el numero de vidas debe ser 6
    
      Examples: 
       
        | dificultad    |   letra   |       
        | facil         |     a     |     
        | media         |     e     |     
        | dificil       |     m     |     
   


 
  Scenario Outline: Reinicia el juego
      Given El jugador inicia el juego
      When Elige "<dificultad>" y hace click en comenzar 
      And El jugador selecciona la letra "<letra>"
      And El jugador reinicia el juego
      And Elige "<dificultad>" y hace click en comenzar 
      Then la palabra a adivinar debe mostrarse con guiones
      And el numero de vidas debe ser 6
    
     Examples: 
        | dificultad    |   letra    |              
        | facil         |     c      |
        | media         |     r      |
        | dificil       |     b      |
