SIMULACIÓN DE CHISGA 

Descripción del Proyecto

Este proyecto simula una chisga o banda musical, en la que se generan aleatoriamente músicos e instrumentos, con un máximo de 10 músicos. Cada músico recibe un instrumento asignado, y luego se pueden realizar diversas operaciones como afinar los instrumentos, verificar su afinación y ejecutar una función musical.

Objetivos

1. Implementación de Buenas Prácticas de Programación y Diseño
   
Este proyecto tiene como principal objetivo aplicar y demostrar el uso de buenas prácticas de programación, enfocándose en
los siguientes principios:

  - SOLID:
     
     Single Responsibility Principle (SRP): Cada clase en el sistema tiene una única responsabilidad. Por ejemplo, la clase         Musico se encarga exclusivamente de gestionar aspectos relacionados con el músico, mientras que la clase Chisga se 
     encarga de la administración del conjunto musical.
     
     Open/Closed Principle (OCP): Las clases están diseñadas para ser abiertas para la extensión pero cerradas para la  
     modificación. Por ejemplo, se pueden añadir nuevos tipos de instrumentos sin necesidad de modificar la clase base 
     Instrumento.

     Liskov Substitution Principle (LSP): Las clases derivadas, como Guitarra o Violin, pueden reemplazar a su clase base 
     Instrumento sin alterar la funcionalidad del programa.

     Interface Segregation Principle (ISP): Los interfaces implementados en las clases se diseñan para evitar que las clases 
     se vean obligadas a implementar métodos que no necesitan.

     Dependency Inversion Principle (DIP): Se invierte la dependencia entre las clases de alto y bajo nivel, promoviendo la 
     utilización de abstracciones.

  - KISS (Keep It Simple, Stupid):

     El código se mantiene simple y directo, evitando complejidad innecesaria. Las funciones y métodos están diseñados para 
     ser claros y fácilmente comprensibles.

  - DRY (Don't Repeat Yourself):
     
     Se minimiza la duplicación de código mediante la reutilización de métodos y la implementación de clases base, como    
     Instrumento.


2. Simulación Realista

Se busca que la simulación sea lo más cercana posible a la realidad de una banda musical, permitiendo:

  - La generación aleatoria de músicos e instrumentos.
  - La afinación y verificación de instrumentos.
  - La organización y ejecución de una función musical.


Requisitos del Proyecto

Para ejecutar este proyecto, se necesita un entorno de desarrollo compatible con:

