nome=input("digite seu nome")
idade=int(input("digite sua idade"))
salario=float(input("digite seu salario"))
porcentagem=float(input("digite a porcentagem"))
aumento=(salario*porcentagem)/100
total=salario+aumento

print (f"seu nome é {nome}, sua idade é {idade} , seu salario é {salario} ,sua porcentagem salarial foi de {porcentagem :.2f},seu aumento salarial foi de {aumento} , seu total é de {total}" )
