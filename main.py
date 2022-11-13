import chaves, conversoes, cifragem

# escolhendo numeros primos

numeroP, numeroQ = 787, 797
produto = numeroP * numeroQ
numeroTotiente = (numeroP - 1) * (numeroQ - 1)

# Fazendo a chave pública e a chave privada

chavePublica = chaves.obterChavePublica(numeroTotiente, produto)
chavePrivada = chaves.obterChavePrivada(chavePublica[0], numeroTotiente, produto)

# escrevendo a mensagem

mensagem = "Alexandre"
mensagem = conversoes.palavraParaNumero(mensagem)

# cifrando mensagem e exibindo na tela

mensagem = cifragem.cifrarMensagem(mensagem, chavePublica)
print(mensagem)

# decifrango mensagem e exibindo na tela

mensagem = cifragem.decifrarMensagem(mensagem, chavePrivada)
mensagem = conversoes.numeroParaPalavra(mensagem)
print(mensagem)
