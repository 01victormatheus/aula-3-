tipo=input("selecione o tipo de combustivel,G para gasolina e E para etanol ")
L=float(input("quantos litros de combustivel voce deseja"))

if tipo=="G" or tipo=="g":
    valor= L*5.80
    print(f"voce pagou {valor} de gasolina")
else:

    if tipo=="E" or tipo== "e":
        valor = L * 4.90
        print(f"voce pagou {valor} de etanol ")

    else:
        print("combustivel não encontrado")

