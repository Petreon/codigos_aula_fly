def uni_total(s):

    soma = 0

    for letras in s:
       soma += ord(letras)

    return soma



if __name__ == "__main__":

    uni_total("dp0b")