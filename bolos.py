bolo = []
sabores_disponiveis = ['Chocolate', 'Maracuja', 'Morango']
tamanhos_disponiveis = ['Pequeno (0.3kg)', 'Médio (0.5kg)', 'Grande (0.7kg)']

msg_inicial = input("[1] Para começar")

def favors():
    print("Sabores disponíveis")
    for sabor in sabores_disponiveis:
        print("Sabor:", sabor)

def size():
    print("Tamanhos disponíveis")
    for tama in tamanhos_disponiveis:
        print(tama)

def montar_bolo():
    sabor = input("Qual o sabor do bolo? ")
    while sabor not in sabores_disponiveis:
        print("Sabor indisponível. Tente novamente.")
        sabor = input("Qual o sabor do bolo? ")
    size()
    tamanho = input("Qual o tamanho do bolo? ")
    while tamanho not in tamanhos_disponiveis:
        print("Tamanho indisponível. Tente novamente.")
        tamanho = input("Qual o tamanho do bolo? ")
    return f"Bolo de {sabor}, tamanho {tamanho}"

favors()
montado = montar_bolo()
print(montado)






