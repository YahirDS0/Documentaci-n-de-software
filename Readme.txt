Readme
# Calculadora de IMC

Esta es una aplicación de calculadora de índice de masa corporal (IMC) desarrollada con Python utilizando la biblioteca tkinter para la creación de interfaces gráficas. La aplicación permite calcular el IMC ajustado de un paciente y guardar los datos en un archivo CSV.

## Requisitos

- Python 3.x
- Bibliotecas adicionales:
  - tkinter
  - PIL (Pillow)
  - csv
  - os

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala la biblioteca Pillow ejecutando el siguiente comando:


## Uso

1. Ejecuta el script `imc_calculadora.py` para iniciar la aplicación.
2. Ingresa los datos del paciente en los campos correspondientes:
- Nombre del paciente
- Peso (kg)
- Altura (m)
- Edad
- Sexo biológico (Hombre o Mujer)
3. Haz clic en el botón "Calcular IMC" para calcular el IMC ajustado del paciente.
4. El resultado del IMC se mostrará en la etiqueta "IMC".
5. Para guardar los datos del paciente en un archivo CSV, haz clic en el botón "Guardar Datos". Los datos se guardarán en un archivo CSV con el nombre del paciente.

## Estructura del código

- `calcular_imc()`: Función para calcular el IMC ajustado del paciente.
- `guardar_datos()`: Función para guardar los datos del paciente en un archivo CSV.
- `configurar_cursor_hand2(event)`: Función para configurar el cursor como hand2 cuando el ratón entra en un botón.

## Archivos de imagen

Asegúrate de tener las siguientes imágenes en la ruta correcta para que la aplicación funcione correctamente:

- `imss.png`: Imagen de fondo de la aplicación.
- `calcular_imc.png`: Imagen para el botón "Calcular IMC".

## Notas

- El archivo CSV se guardará en el directorio actual con el nombre del paciente como nombre de archivo.
- Si el archivo CSV ya existe, los datos se añadirán al final del archivo.

## Ejecución

Para ejecutar la aplicación, utiliza el siguiente comando en tu terminal:


## Autor

Desarrollado por Yahir Delgado


	