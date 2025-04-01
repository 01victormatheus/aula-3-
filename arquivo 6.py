t1=input("nome do time 1")
t2=input("nome do time 2")
print(t1,t2)

golst1=int(input(f"numero de gols marcados por {t1}:"))
golst2=int(input(f"numero de gols marcados por {t2}:"))

if golst1>golst2:
        print (f" o {t1} ganhouu")
else:
    if golst1 == golst2:
        print("EMPATE")
    else:
        print(f"o {t2} ganhou ")

