def palavraParaNumero(palavra):

    palavraConvertida = []

    for letra in palavra:
        palavraConvertida.append(ord(letra))
    
    return palavraConvertida

def numeroParaPalavra(palavraConvertida):
    
    palavra = ''

    for numero in palavraConvertida:
        palavra += chr(numero)
    
    return palavra
    