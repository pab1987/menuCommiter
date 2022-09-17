contador = 0

while(contador != 5):
    print("MENÚ")
    print("*****************")
    print("1. Recibir nombre y año de nacimiento")
    print("2. calcular edad y mostrar en pantalla")
    print("3. mostrar saludo de buenas noches al usuario")
    print("4. contarle cuantos años tendra en el 2030")
    print("5. SALIR")
    print("*****************")
    
    
    nombre = None
    anoNacimiento = None
    anoActual = 2022
    edad = None
    
    contador = int(input("Digita la opcion del menú"))
    
    if contador == 1:
        nombre = input('Digita el nombre completo: ')
        anoNacimiento = int(input('Ingrese su año de nacimiento: '))
    elif contador == 2:
        edad = anoActual - anoNacimiento
        print(f"La edad de {nombre} es de {edad} años.")
        
        
        
