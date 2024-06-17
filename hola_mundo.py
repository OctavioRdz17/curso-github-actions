# crear un script que diga ""Hola mundo"" en la consola
# y que se ejecute desde la terminal

import os

def main():
    nombre = os.getenv("USERNAME")
    print(F"Hola {nombre} desde Github!")

if __name__ == "__main__":
    main()


