'''/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */'''


def par (num):
    return num % 2 == 0

def primo(num):
    for i in range(1,num):
        if num % i == 0:
            return True
        
    return False


numero = int(input('Introduce un número: '))
print(str(numero) + ' es primo' if primo(numero) else ' no es primo, ')