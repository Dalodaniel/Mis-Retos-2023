'''/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */'''


import random


def gen_contr(long):
    characters = list(range(33,123))

    contr = ''

    while len(contr) < long:
        contr += chr(random.choice(characters))

    return(contr)



longitud = random.randint(8,16)
print(gen_contr(longitud))