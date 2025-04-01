n1=float(input("digite uma nota"))
n2=float(input("digite uma nota"))
n3=float(input("digite uma nota"))

media=(n1+n2+n3)/3

if media>=7:
        print(f"aluno aprovado por media {media}")

else:
    if media<4:
        print(f"aluno reprovado por media {media}")
    else:
        print(f"aluno recuperaçao com media {media}")

