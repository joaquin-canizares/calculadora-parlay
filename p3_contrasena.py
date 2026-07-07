def pedir_contrasena():
    while True:
        contrasena = input("Ingrese la contrasena: ")
        tiene_numero = False
        mayuscula = False
        minuscula = False
        simbolo = False
        puntos = 0
        longitud = len(contrasena)
        if longitud >=8:
            puntos +=1
        for letra in contrasena:
            if letra.isdigit():
                tiene_numero = True
            if letra.isupper():
                mayuscula = True
            if letra.islower():
                minuscula = True
            if letra.isalnum() == False:
                simbolo = True
        if tiene_numero:
            print("Tiene numero")
            puntos += 1
        else:
            print("No tiene numero")
        if mayuscula:
            print("Tiene mayuscula")
            puntos += 1
        else:
            print("No tiene mayuscula")    
        if minuscula:
            print("Tiene minuscula")
            puntos += 1
        else:
            print("No tiene minuscula") 
        if simbolo:
            print("Tiene simbolo")
            puntos += 1
        else:
            print("No tiene simbolo") 
        if puntos >= 5:
            print("Contraseña ACEPTADA")
            break
        else:
            print("Contraseña poco segura, ingrese nuevamente")


pedir_contrasena()

