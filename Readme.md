# FALLDETEKTOR 2.0
---
### *Introducción a la Inteligencia Artificial*
### *Septiembre de 2019*
## Integrantes

* Daniel Amaris(ddamarisr@unal.edu.co) - Ciencias de la Computacion
* Christian Ortiz(cfortizp@unal.edu.co) - Ingenieria de Sistemas
## Descripción

Uno de los problemas más comunes que tienen los adultos mayores y sus familiares son las caídas. Este problema ha conducido a los adultos mayores a lesiones, discapacidades e incluso la muerte.

Uno de los problemas más graves de las caídas es que la gran mayoría de ellas no son reportadas, se estima que el 80% de las caídas se producen en el hogar y el 20% restante fuera del él, también se sabe que un quinto de los adultos mayores de entre 65 a 69 años, y hasta dos quintos de los mayores de 80, sufren una caída en el último año.

Así mismo existen las principales causas de caídas en el adulto mayor, son de tipo fisiológico, propias del envejecimiento, como la pérdida de masa muscular, disminución de la percepción de sensibilidad profunda, reducción de rango articular, problemas de visión. También se deben a problemas de tipo patológico, enfermedades como el Parkinson, alteraciones de la visión, secuelas de un accidente vascular cerebral y demencia.

Actualmente existen diversos mecanismos para detectar las caídas, dispositivos electrónicos como el Angel4, Elea y Nursecall, pueden llegar a costar 149,95€ alrededor de 560.453,12 COP. También se pueden encontrar en las tiendas virtuales como la Play Store y la App Store aplicaciones como Chk-In Fall y FallDetector que realizan esta tarea.

El principal objetivo de este proyecto es desarrollar en Python un dispositivo capaz de detectar caídas en tiempo real. Para esto se realizó un agente que fue entrenado en diferentes situaciones. A continuación, se hará un reporte sobre el proyecto realizado.
## Metodología

El objetivo principal de nuestro proyecto consiste en interpretar los datos provenientes de un sensor (en este caso el acelerómetro de un celular) y establecer si ha ocurrido una caída. Para tal fin, desarrollamos en nuestro código un módulo encargado de recibir "escuchar" los datos provenientes del celular tales como los datos de aceleración en los tres ejes (x,y,z) y los datos de latitud y longitud correspondientes. Luego desarrollamos un módulo para la comunicación con el usuario (una interfaz) y finalmente diseñamos un módulo para aprendizaje y reconocimiento
### Módulo de captación de datos y filtrado: 
