'''/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */'''


def par (num):
    return num % 2 == 0

def primo(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        
    return True

def fibonacci(num):
    val = 1
    val_ant = 0
    temp = 0
    while val < num:
        temp = val
        val = val + val_ant
        val_ant = temp
        if val == num:
            return True

    if num == 0 or num == 1:
        return True
    else:
        return False


numero = int(input('Introduce un número: '))
print('El número ' + str(numero) + ' es primo' if primo(numero) else 'El número ' + str(numero) + ' no es primo.')
print('El número ' + str(numero) + ' es par' if par(numero) else 'El número ' + str(numero) + ' no es par.')
print('El número ' + str(numero) + ' es fibonacci' if fibonacci(numero) else 'El número ' + str(numero) + ' no es fibonacci.')