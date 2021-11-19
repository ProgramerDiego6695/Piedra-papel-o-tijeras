#piedra papel o tijeras por Diego Emiliano
#disfruta el juego
#las variables p_jugador y p_computado son inutiles porque todavia no añado el sistema para poder ganar

#importar el paquete "random"
import random
#crear una tupla con los movimientos disponibles
movimientos = ("piedra", "papel", "tijeras")
#crear la variable "p_computadora"
p_computadora = 0
#crear la variable p_jugador
p_jugador = 0
#poner el disclaimer
print("DISCLAIMER: cuando quieras dejar de jugar espere cuando se muestre el texto de piedra papel o tijeras y escriba Q")
input()


#crear la funcion cuerpo
def cuerpo():
    #pedirle al jugador que elija piedra, papel o tijeras
    print("piedra papel o tijeras")
    #pedirle al jugador su movimiento
    movimientoJugador = input()
    #elejir el movimiento de la maquina
    movimientoComputadora = random.choice(movimientos)
    #si el jugador elije piedra y la computadora elije papel, pierdes la ronda
    if movimientoJugador == "piedra" and movimientoComputadora == "papel":
        print("la Computadora eligio papel, perdiste la ronda")
        input()
        cuerpo()
    #si el jugador elije piedra y la computadora elige tijeras, ganas la ronda
    if movimientoJugador == "piedra" and movimientoComputadora == "tijeras":
        print("la computadora eligio tijeras, ganaste la ronda")
        input()
        cuerpo()
    #si el jugador elige papel y la computadora elige tijeras, pierdes la ronda
    #PD: esta parte la voy a optimizar en el futuro
    if movimientoJugador == "papel" and movimientoComputadora == "tijeras":
        print("la computadora a elegido tijeras, perdiste la ronda")
        input()
        cuerpo()
    #si el jugador elige papel y la computadora elige piedra, ganas la ronda
    if movimientoJugador == "papel" and movimientoComputadora == "piedra":
        print("la computadora a elegido piedra, ganaste la ronda")
        p_jugador =+ 1
        input()
        cuerpo()
    #si el jugador elige papel y la computadora elige piedra, pierdes la ronda
    if movimientoJugador == "tijeras" and movimientoComputadora == "piedra":
        print("la computadora a eligido piedra, perdiste la ronda")
        p_computadora =+ 1
        input()
        cuerpo()
    #si el jugador elige tijeras y la computadora elije papel, ganas la ronda
    if movimientoJugador == "tijeras" and movimientoComputadora == "papel":
        input()
        cuerpo()
    #si la computadora y tu han elegido lo mismo, dar un empate
    if movimientoJugador == movimientoComputadora:
        print("la computadora y tu han elegido lo mismo, empate")
        input()
        cuerpo()
    #empezar un bucle para terminar el juego
    while True:
        #ver si cuando el jugador cuando va a elegir el movimiento escribe Q o q, acabar el juego
        if movimientoJugador == "Q":
            print("Gracias por jugar")
            input()
            quit()





cuerpo()