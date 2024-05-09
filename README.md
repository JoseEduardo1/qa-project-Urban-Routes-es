# Urban Routes Testing Project

Este proyecto contiene pruebas automatizadas para la aplicación Urban Routes. Utiliza Selenium y Python para realizar pruebas de funcionalidad en la aplicación.

## Setup

Para ejecutar las pruebas en este proyecto, asegúrate de tener Python 3.12 instalado, la version de Selenium 4.20.0 y pytest version 8.2.0. 
Tambien asegurate de tener el navegador Google Chrome ya que sera el navegador utilizado para correr las pruebas

## Descripción del Proyecto
El propósito de este proyecto es realizar pruebas automatizadas en la aplicación Urban Routes para garantizar su funcionalidad y fiabilidad. Las pruebas están diseñadas para probar diferentes aspectos de la aplicación, desde la introducción de direcciones hasta la interacción con los diferentes elementos de la interfaz de usuario.

## Configuración
data.py: se definen las variables globales utilizadas en las pruebas  
helpers.py: Contiene una función que devuelve el código de confirmación de teléfono
pages.py: Define la estructura de la página de la aplicación, incluyendo localizadores y metodos.
test_UrbanRoutes.py: Contiene las pruebas automatizadas para la aplicación Urban Routes

## Uso
Para ejecutar las pruebas es necesario configurar pytest de modo que se ejecuten todas las pruebas del archivo test_UrbanRoutes.py

## Contribución
Si deseas contribuir a este proyecto, no dudes en abrir una solicitud de extracción. Todas las contribuciones son bienvenidas.

## Recomendacion importante
La funcion retrieve_phone_code que se encuentra dentro de helpers.py fue adecuada a la nueva version de selenium, de correr una version mas antigua de la recomendada en este proyecto pueden ocurrir errores.
