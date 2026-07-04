import random
def patear():
    goles = 0
    atajadas = 0
    for i in range (5):
        direccion = random.randint(1,3)
        lado = int(input("DISPARAR: 1=izquierda, 2=centro, 3=derecho: "))
        if lado == direccion:
            print("FALLASTE!!!")
        else:
            print ("GOLAZO!!!")
            goles = goles+1
        direccion_simulacion = random.randint(1,3)
        atajar = int(input("ATAJAR: 1=izquierda, 2=centro, 3=derecho: "))
        if direccion_simulacion != atajar:
            print("GOL")
        else:
            print("Penal atajado!!!")
            atajadas += 1
    print("Has marcado estos goles: ", goles)  
    print("Has atajado estos tiros: ", )         

    
patear()    