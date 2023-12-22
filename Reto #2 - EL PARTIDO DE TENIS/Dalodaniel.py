'''/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */'''



secuencia = input("Introduce la secuencia de puntos: ")
# Introducimos la secuancia en una lista
lista_sec = secuencia.split(',')

contad_1 = 0
contad_2 = 0
dict = {0:'Love', 1:'15', 2:'30', 3:'40'}

for i in range(0, len(lista_sec)):
    if lista_sec[i] == 'P1':
        contad_1 += 1
    elif lista_sec[i] == 'P2':
        contad_2 += 1

    if contad_1 > 3 or contad_2 > 3:
        if contad_1 == contad_2:
            print('Deuce')
        elif contad_1 > contad_2 and (contad_1 - contad_2 == 1):
            print('Ventaja P1')
        elif contad_1 > contad_2 and (contad_1 - contad_2 == 2):
            print('Ha ganado el P1')
        elif contad_2 > contad_1 and (contad_2 - contad_1 == 1):
            print('Ventaja P2')
        elif contad_2 > contad_1 and (contad_2 - contad_1 == 2):
            print('Ha ganado el P2')

    else:
        print (dict[contad_1] + ' - '+ dict[contad_2])  


