def cifrarMensagem(mensagem, chavePublica):
    
    mensagemCifrada = []

    for letra in mensagem:
        mensagemCifrada.append((letra ** chavePublica[0]) % chavePublica[1])
    
    return mensagemCifrada


def decifrarMensagem(mensagemCifrada, chavePrivada):
    
    mensagem = []

    for letra in mensagemCifrada:
        mensagem.append((letra ** chavePrivada[0]) % chavePrivada[1])
    
    return mensagem
    