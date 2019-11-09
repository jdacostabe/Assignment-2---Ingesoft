# Assignment 2 - Software Engineering II

## Patrón: Hollywood principle

#### Breve descripción del patrón:
El patrón de inversión de control (IoC), también conocido como “Hollywood Principle”, es un patrón que tiene como objetivo hacer que el software sea más escalable, modular, reutilizable y fácil de mantener. Este patrón consiste en especificar respuestas deseadas a sucesos o solicitudes de datos concretas, dejando que algún tipo de entidad o arquitectura externa lleve a cabo las acciones de control que se requieran en el orden necesario y para el conjunto de sucesos que tengan que ocurrir.
#### Contenido
Dentro del repositorio se encontraran dos archivos:
 * **implementacion.py:** Se realiza la implementación general, explicando su funcionamiento e importancia.
 * **ejemplo.py:** Se lleva la explicación anterior a un caso práctico. Se tiene una cuenta de un banco, la cual tiene 3 estados (Deuda, Neto, Ganancia). El patrón Hollywood Principle es usado al considerar que cada sucursal del banco puede controlar a su manera los estados de la cuenta.
 Inicialmente en casos de error el algoritmo del banco arrojaba una excepción para que la sucursal la controlara a su manera. Pero con el uso del principio de Hollywood todo es muy claro, existe un algoritmo base que necesita 3 funciones que se ejecutarán en cada uno de los estados, estas son definidas por la sucursal.