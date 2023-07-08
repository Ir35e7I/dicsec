# dicsec

      ██████  ▒█████   ███▄    █ ▓█████▄  ▄▄▄          ▄▄▄       ███▄    █  ▄▄▄       ██▀███   ██ ▄█▀ ▒█████  
    ▒██    ▒ ▒██▒  ██▒ ██ ▀█   █ ▒██▀ ██▌▒████▄       ▒████▄     ██ ▀█   █ ▒████▄    ▓██ ▒ ██▒ ██▄█▒ ▒██▒  ██▒
    ░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒░██   █▌▒██  ▀█▄     ▒██  ▀█▄  ▓██  ▀█ ██▒▒██  ▀█▄  ▓██ ░▄█ ▒▓███▄░ ▒██░  ██▒
      ▒   ██▒▒██   ██░▓██▒  ▐▌██▒░▓█▄   ▌░██▄▄▄▄██    ░██▄▄▄▄██ ▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▀▀█▄  ▓██ █▄ ▒██   ██░
    ▒██████▒▒░ ████▓▒░▒██░   ▓██░░▒████▓  ▓█   ▓██▒    ▓█   ▓██▒▒██░   ▓██░ ▓█   ▓██▒░██▓ ▒██▒▒██▒ █▄░ ████▓▒░
    ▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒▒▓  ▒  ▒▒   ▓▒█░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▒ ▓▒░ ▒░▒░▒░ 
    ░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ▒  ▒   ▒   ▒▒ ░     ▒   ▒▒ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒ ▒░  ░ ▒ ▒░ 
    ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░  ░ ░  ░   ░   ▒        ░   ▒      ░   ░ ░   ░   ▒     ░░   ░ ░ ░░ ░ ░ ░ ░ ▒  
          ░      ░ ░           ░    ░          ░  ░         ░  ░         ░       ░  ░   ░     ░  ░       ░ ░  
                                      ░                                                                           
 
generador de contraseñas o palabras para ataques de fuerza bruta

La función de este codigo es generar un diccionario de combinaciones de palabras y caracteres especiales. El diccionario se genera a partir de un listado de palabras importantes proporcionado en un archivo de texto. El usuario puede especificar la ubicación del archivo, la longitud máxima de las palabras generadas y otros parámetros opcionales, como la inserción de números y combinaciones de caracteres especiales.

En cuanto a los patrones utilizados en el código:

1. Estructura general del programa: El código sigue una estructura modular, dividiendo las diferentes funcionalidades en funciones separadas.
2. Uso de funciones: Se definen múltiples funciones para realizar tareas específicas, lo que permite un mejor diseño y reutilización del código.
3. Uso de estructuras de control: Se utilizan estructuras de control como bucles `for` y `if` para iterar sobre elementos y tomar decisiones basadas en condiciones.
4. Manipulación de cadenas: Se utilizan diferentes métodos y operaciones para manipular y combinar cadenas de texto, como `join`, `lower`, `capitalize` y `[::-1]`.
5. Uso de módulos externos: Se importan y utilizan módulos externos como `itertools`, `datetime` y `random` para acceder a funcionalidades adicionales.
6. Manipulación de archivos: Se utiliza la lectura y escritura de archivos para obtener palabras del archivo de entrada y generar el diccionario de combinaciones en archivos de salida.
7. Uso de entrada/salida de usuario: El código interactúa con el usuario mediante la función `input` para solicitar información y mostrar mensajes.

Uso
1. Una vez clonado el repositorio se debe tener un archivo .txt dentro del cual deben estar un listado de palabras basico resultado del proceso se OSINT
2. se ejecuta la aplicación con el comando python3 dicsec.py

se ha probado poniendo el listado de palabras resultado por osint dentro de la misma carpeta donde se ubica dicsec.py, colocando soli el nombre del archivo txt

Notas:
dicsec.py genera diferentes archvos .txt para el uso de fuerza bruta,expotando un maximo de lineas; esto con el fin de que no sature los recursos del sistema