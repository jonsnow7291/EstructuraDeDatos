# Ejercicios de Recursividad y Operaciones Básicas (MVC)

Autores: **Juan Diego Chaparro**, **Angy Rivas**, **Karen Ravelo**  
Fecha: 24/09/2025

Este conjunto de ejercicios implementa diferentes problemas clásicos y educativos usando el patrón **Modelo - Vista - Controlador (MVC)** en Python. Cada ejercicio cuenta con:
- **Modelo**: Lógica de negocio / cálculo.
- **Vista**: Entrada y salida con el usuario.
- **Controlador**: Coordina la interacción entre modelo y vista.

## Lista de Ejercicios

1. **Sucesión de Fibonacci**  
   Cálculo recursivo del n-ésimo número de Fibonacci (versión simple).  
2. **Suma de enteros 0..n**  
   Usa fórmula cerrada n(n+1)/2.  
3. **Producto de dos enteros**  
   Multiplicación con validación de tipos.  
4. **Potencia base^exponente**  
   Implementación recursiva optimizada (exponentiación binaria).  
5. **Invertir cadena**  
   Invierte una secuencia de caracteres.  
6. **Serie armónica h(n)**  
   Suma 1 + 1/2 + ... + 1/n (implementación iterativa; alternativa recursiva en comentarios).  
7. **Logaritmo entero floor_b(n)**  
   Calcula el logaritmo entero mediante divisiones sucesivas.  
8. **Sucesión f(1)=2; f(n)=1/(n + f(n-1))**  
   Definida recursivamente con acumulación descendente.  
9. **Torres de Hanoi**  
   Genera y muestra los pasos para mover n discos entre varillas.  
10. **Sucesión f(1)=2; f(n)=f(n-1)+2n**  
    Sucesión aritmética recursiva (posee forma cerrada n(n+3)).  

## Estructura de Carpetas

```
controller/   -> Controladores de cada ejercicio
model/        -> Modelos con la lógica de cálculo
view/         -> Vistas (entrada/salida)
main.py       -> Menú principal para ejecutar los ejercicios
```

## Ejecución

Desde la carpeta que contiene `main.py`:

```powershell
python .\main.py
```

Luego selecciona una opción del menú (1 a 10) o 0 para salir.

## Estándares y Estilo
- Cada archivo contiene un encabezado con autores y descripción.
- Las validaciones básicas devuelven mensajes de error como cadenas en lugar de levantar excepciones (en una versión futura se puede estandarizar).
- Se utiliza recursión directa sin memoización para mantenerlo didáctico.

## Mejoras Futuras (Sugeridas)
- Unificar manejo de errores con excepciones personalizadas.
- Añadir pruebas unitarias (pytest) para modelos.
- Implementar memoización para Fibonacci.
- Hacer el menú data-driven (lista de tuplas o registro dinámico).
- Internacionalización (i18n) si se requiere otro idioma.

## Licencia
Uso educativo. Ajustar según necesidad institucional.

---
¿Necesitas que agreguemos algo más? Pide y lo expandimos.
