def calcularMDC(numeroX, numeroY):
    while(numeroY):
        numeroX, numeroY = numeroY, numeroX % numeroY
    
    return numeroX


def inversoModular(expoente, totiente):
    for inverso in range(1, totiente):
        if (((expoente % totiente) * (inverso % totiente)) % totiente == 1):
            
            return inverso
    
    return -1
