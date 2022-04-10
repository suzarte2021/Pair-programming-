##[Questão 25] Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
##
pontos = 0

print("Responda apenas com sim ou não: ")

a=str(input("Telefonou para a vítima? "))

if a == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

b=str(input("Esteve no local do crime?  "))

if b == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

c=str(input("Você mora perto da vítima?  "))

if c == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

d=str(input("Você devia para a vítima?  "))

if d == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

e=str(input(" Você já trabalhou com a vítima?  "))

if e == 'sim':

 pontos = pontos + 1

else:

 pontos = pontos + 0

print()

print(f"você fez {pontos} pontos")

if pontos == 2:

 print("Classificado como: Suspeito")

if pontos == 3 or pontos == 4:

 print("Classificado como: Cúmplice")

if pontos == 5:

 print("Classificado como: Assassino")

elif pontos == 0:

 print("Classificado como: Inocente")

