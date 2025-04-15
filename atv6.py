pin = 1234
tentativa = 1
mensagem = "Acesso bloqueado!"
while tentativa <=3:
    senha = int(input("Digite sua senha: "))
    if senha == pin:
        mensagem = ("Login efetuado com sucesso!")
        break
    tentativa = tentativa +1
print (mensagem)