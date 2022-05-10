def inverso_do_modulo(e, remainder):
    _remainder = remainder
    y = 0
    x = 1

    if remainder == 1:
        return 0

    while e > 1:
        quociente = e // remainder
        t = remainder

        remainder = e % remainder
        e = t
        t = y

        y = x - quociente * y
        x = t

    if x < 0:
        x = x + _remainder
    return x


def codificar(public_key, plaintext):
    e, n = public_key
    chipertext = []

    for char in plaintext:
        letra = ord(char)
        chipertext.append(pow(letra, e, n))
    return chipertext


def decodificar(private_key, chipertext):
    d, n = private_key
    plaintext = ''

    for char in chipertext:
        letra = pow(char, d, n)
        plaintext = plaintext + str(chr(letra))
    return plaintext
