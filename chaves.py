from matematica import calcularMDC, inversoModular

def obterChavePublica(totiente, produto):

    for numero in reversed(range(totiente)):
        if calcularMDC(totiente, numero) == 1:
            chavePublica = (numero, produto)
            break
    
    return chavePublica


def obterChavePrivada(expoente, totiente, produto):

    chavePrivada = (inversoModular(expoente, totiente), produto)
    
    return chavePrivada
    