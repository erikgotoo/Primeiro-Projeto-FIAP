AULA 2 PYTHON:
'''
#uso de verdadeiro ou falso
primeiro_numero = 2
segundo_numero = 3

a = primeiro_numero > segundo_numero
b = segundo_numero < primeiro_numero
c = primeiro_numero >= segundo_numero
d = primeiro_numero <= primeiro_numero
e = primeiro_numero != segundo_numero
print (f"A comparação do {primeiro_numero} > {segundo_numero} dá {a}")
print (f"A comparação do {segundo_numero} < {primeiro_numero} dá {b}")
print (f"A comparação do {primeiro_numero} >= {segundo_numero} dá {c}")
print (f"A comparação do {segundo_numero} <= {primeiro_numero} dá {d}")
print (f"A comparação do {primeiro_numero} != {segundo_numero} dá {e}")


a = 2
b = 3
c = 4
d = 5
#or
print(f"A comparação {a}>{b} or {c}>{d}, ou seja, {a>b} or {c>d} dá {a>b or c>d}")
print(f"A comparação {b}>{a} or {c}>{d}, ou seja, {b>a} or {c>d} dá {b>a or c>d}")
print(f"A comparação {a}>{b} or {d}<{c}, ou seja, {a>b} or {d>c} dá {a>b or d>c}")
print(f"A comparação {c}>={b} or {a}>{c}, ou seja, {c>=b} or {a<c} dá {a<b or d>c}\n")
#and
print(f"A comparação {a}>{b} and {c}>{d}, ou seja, {a>b} or {c>d} dá {a>b and c>d}")
print(f"A comparação {b}>{a} and {c}>{d}, ou seja, {b>a} or {c>d} dá {b>a and c>d}")
print(f"A comparação {a}>{b} and {d}>{c}, ou seja, {a>b} or {d>c} dá {a>b and d>c}")
print(f"A comparação {c}>={b} and {a}>{c}, ou seja, {c>=b} or {a<c} dá {a>=b and a<c}")

#checando idade if(caso tenha) else(caso contrario)
idade = int(input("Diga sua idade: "))
if idade < 18:
    print("Você não deve usar o Ze Delivery")
else:
    print("Bem vindo ao Ze Delivery")

#vaga de prioridade (or) ser isso ou ser aquilo
idoso = input("Você é idoso ?")
gestante = input("Você é gestante ?")
if idoso == 'sim' or gestante == 'sim':
    print("Pode estacionar")

#vaga de estacionar (and) ter isso e ser isso
idoso = input("Você é idoso?")
cartao = input("Você tem o cartao?")
if idoso == 'sim' and cartao == 'sim' :
  print("Pode estacionar.")
'''
letra = input("Diga uma letra:")
if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
   print(F"{letra} é uma Vogal")
else:
   print(F"{letra} é uma Consoante")
'''
AULA 8 PYTHON
'''
#Exercicio 1
numero = input("Diga seu numero: ")
while True:
    if numero.isnumeric():
      #if(0 <= int(numero) >= 10):
      if int(numero) > 0 and int(numero) < 10:
        numero = int(numero)
        break
        print("Numero invalido")
    print("Precisa ser numero")
print("Numero de merda!")


#Exercicio 2
nome = input("Diga o seu nome: ")
while len(nome) < 3:
    nome = input("Diga o seu nome com mais de 3 letras: ")

while True:
    idade = input("Diga a sua idade: ")
    if idade.isnumeric():
        idade = int(idade)
        if idade < 150:
            break
    print("Opção Inválida")

salario = input("Diga o seu salario: ")
while not salario.isnumeric():
    print("Opção Inválida")
    salario = input("Diga o seu salario: ")

sexo = input("Diga seu sexo em f ou m: ")
while not (sexo == 'f' or sexo == 'm'): #while sexo != 'f' and sexo == != 'm':
    print("Opção Inválida")
    sexo = input("Diga seu sexo em f ou m: ")

estadocivil = input("Diga seu estado civil: s,c,v ou d: ")
while not (estadocivil == 's' or estadocivil == 'c' or estadocivil == 'v' or estadocivil == 'd'):
    print("Opção Inválida")
    estadocivil = input("Diga seu estado civil: s,c,v ou d: ")



#Exercicio 3
a = 80
b = 200
tempo = 0
while a < b:
    a*= 1.03
    b*= 1.015
    tempo += 1
print(tempo)



#Exercicio 4
quantidade = 0
soma = 0
while quantidade < 5:
    numero = input(f"Diga o {quantidade+1} numero: ")
    while not numero.isnumeric():
        print("NUMERO BURRO!")
        numero = input(f"Diga o {quantidade+1} numero: ")
    numero = int(numero)
    soma += numero
    quantidade += 1
print(f"A soma é {soma}")
print(f"A media é {soma/quantidade}")




#Exercicio 5
a = int(input("Diga um numero: "))
b = int(input("Diga um outro numero: "))

while a < b:
    print(a)
    a+=1

while b < a:
    print(b)
    b+=1
'''

'''
#Exercicio 6
nome = input("Diga a porra do seu nome: ")
senha = input("Diga a porra da sua senha: ")
while nome == senha:
    print("A porra da senha nao pode ser igual a porra do nome krl")
    nome = input("Diga a porra do seu nome: ")
    senha = input("Diga a porra da sua senha: ")
print("Agora sim krl")

#Exercicio 7
numero = int(input("Digite seu numero: "))
multiplicador = 1
while numero < 1 or numero > 10:
    numero = int(input("Digite seu numero: "))
while True:
    final = numero * multiplicador
    print(f"{numero} X {multiplicador} = {final}")
    multiplicador += 1
    if multiplicador > 10:
        break

#Exercicio 7 mas com todas as tabuadas de 1 a 10:
numero = 1
while numero <= 10:
    i = 1
    print(f"Tabuada do {numero}")
    while i <= 10:
        print (f"{numero}*{i} = {numero*i}")
        i += 1
    numero += 1
    print()

#Exercicio 8
numero = int(input("Digite seu numero: "))
n1 = 1
n2 = 1
i = 1
print(n1)
while i < numero:
    print(n2)
    aux = n1+n2
    n1 = n2
    n2 = aux
    i += 1

#Exercicio 9
i = 0
pares = 0
impares = 0
while i < 10:
    numero = input("Diga o seu {i+1}° numero: ")
    while not numero.isnumeric():
        print("Diga apenas numero krl")
        numero = input("Diga o seu numero: ")
    numero = int(numero)
    if numero % 2 == 0:
        pares += 1
    i += 1
    print(f"{pares} pares e {i-pares} impares")

#Exercicio 9 com continue
quantidade = 0
impar = 0
par = 0
while quantidade < 10:
 numero = (input(f"Diga o seu {quantidade+1}° numero: "))
 if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        par += 1
        quantidade += 1
        continue
    print("IMPAR!")
    impar += 1
    quantidade += 1
print(f"São {par} pares e {impar} impares!")

#Exercicio 10
numero = input("Diga o seu numero: ")
if numero.isnumeric():
   numero = int(numero)
fatorial = numero
fatorial_string = f"{numero}! = {numero}"
while numero > 1:
    numero -= 1
    fatorial *= numero
    fatorial_string += f"*{numero}"
fatorial_string += f" = {fatorial}"
print(fatorial_string)

#Exercicio 11
i = 2
numero = input("Diga o seu numero: ")
if numero.isnumeric():
   numero = int(numero)
while i < numero/2:
    print(f"{numero}%{i}={numero%i}")
    if numero % i == 0:
        print(f"{numero} não é primo!")
        break
    i += 1
if i >= numero/2:
    print(f"{numero} é primo")

#Exercicio 11 outro jeito
i = 2
numero = input("Diga o seu numero: ")
if numero.isnumeric():
   numero = int(numero)
while i < numero**0.5:
    print(f"{numero}%{i}={numero%i}")
    if numero % i == 0:
        print(f"{numero} não é primo!")
        break
    i += 1
if i >= numero**0.5:
    print(f"{numero} é primo")

#Exercicio 13
ano = input("Diga o seu numero: ")
if ano.isnumeric():
   ano = int(ano)
salario = 1000
partida = 1995
taxa = 0.015
while partida < ano:
    salario *= 1 + taxa
    taxa *= 2
    partida += 1
print(salario)
'''
#Exercicio 14
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

while True:
   numero = input("Diga o seu numero (>100 para sair): ")
   if numero.isnumeric():
     numero = int(numero)
     if numero <= 25:
      intervalo1 += 1
     elif numero <= 50:
      intervalo2 += 1
     elif numero <= 75:
      intervalo3 += 1
     elif numero <= 100:
      intervalo4 += 1
     else:
          break
   else:
    print("Coloca um numero krl")
print(f"Há {intervalo1} numeros no primeiro intervalo 0-25\n"
 f"Há {intervalo2} numeros no segundo intervalo 26-50\n"
 f"Há {intervalo3} numeros no terceiro intervalo 51-75\n"
 f"Há {intervalo4} numeros no quarto intervalo 76-100")
'''
#Exercicio 15
participante1 = 0
participante2 = 0
participante3 = 0
participante4 = 0
branco = 0
nulo = 0
total = 0
while True:
    voto = input("Diga o seu voto \n0-Sair\n1-Danilo\n2-Erik\n3-Mineiro\n4-Lorenzo \nEscolha: ")
    if not (voto == "0" or voto == "1" or voto == "2" or voto == "3" or voto == "4" or voto == "5" or voto == "6"):
      print("Erro!")
      continue
    if voto == "0":
     break
    elif voto == "1":
      participante1 += 1
    elif voto == "2":
      participante2 += 1
    elif voto == "3":
      participante3 += 1
    elif voto == "4":
      participante4 += 1
    elif voto == "5":
      branco += 1
    elif voto == "6":
      nulo += 1
    total += 1

if total!=0:
 print(f"Há {participante1} votos no Danilo, {100*participante1/total:.2f}% dos votos\n"
      f"Há {participante2} votos no Erik, {100*participante2/total:.2f}% dos votos\n"
      f"Há {participante3} votos no Mineiro, {100*participante3/total:.2f}% dos votos\n"
      f"Há {participante4} votos no Lorenzo, {100*participante4/total:.2f}% dos votos\n"
      f"Há {branco} votos brancos, {100*branco/total:.2f}% dos votos\n"
      f"Há {nulo} votos nulos, {100*nulo/total:.2f}% dos votos\n"
      f"Há {total} votos totais \n")

 #(100*brancos/total:.2f)%


AULA 9 ALGUNS EXEMPLOS DE USO PARA O FOR
'''
1-
nomes = ["erik", "mineiro","wendell"]
for nome in nomes:
    print(nome)

2-
for i in range(1,15,2) #(começo,quantidade,pula de tanto em tanto):
    print(i)

3-
for i in range(10):
    print(i,end= " ")
    i = 1
    print(i)

4-
for i in range (10):
    if i%2 == 0:
        print(f"{i} é par")
    else:
        print(f"{i} é impar")

5-
i = 0
frase = "A CABECA DA MINHA PIKA"
for char in frase:
i += 1
print(i)

6- mesmo que o 5 com frase e sem contar o espaço 
i = 0
frase = "A CABECA DA MINHA PIKA"
for char in frase:
    if char != " ":
     i += 1
print(i)

=============================================

vogais = 0
for char in 'erik':
    print(char, end= '')
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vogais += 1
print(f", essa palavra possue {vogais} vogais")

senha_cadastrada = "1234"
for i in range (3):
    senha = input("Diga a sua senha: ")
    if senha == senha_cadastrada:
        print("Seja Bem Vindo!")
        break
    print(f"So mais {2-i} tentativas!")
if senha != senha_cadastrada:
    print("Vaza!")

pares = 0
impares = 0
quantidade = 0
for i in range(10):
    numero = (input(f"Diga o seu {i+1}° numero: "))
    if not numero.isnumeric():
        numero = (input(f"Diga o seu {i+1}° numero: "))
    numero = int(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"São {pares} pares e {impares} impares!")

soma = 0
quantidade = 0
quantos = int(input("Diga quantos numeros vc deseja digitar: "))
for i in range(quantos):
    numero = (input(f"Diga o seu {i+1}° numero: "))
    if not numero.isnumeric():
        numero = (input(f"Diga o seu {i+1}° numero: "))
    numero = int(numero)
    soma += numero
    quantidade += 1
print(f"A soma é {soma}")
print(f"A media é {soma/quantidade}")
'''

AULA 10 MAIS FOR - E LISTA!!
'''
comprimento = 0
for char in 'danilo':
    comprimento += 1
print(comprimento)

#Exercicio 1
soma = 0
quantidade = 0
quantos = int(input("Diga quantos numeros vc deseja digitar: "))
for i in range(quantos):
    numero = (input(f"Diga o seu {i+1}° numero: "))
    if not numero.isnumeric():
        numero = (input(f"Diga o seu {i+1}° numero: "))
    numero = int(numero)
    soma += numero
    quantidade += 1
print(f"A soma é {soma}")
print(f"A media é {soma/quantidade}")

#Exercicio 2
pares = 0
impares = 0
quantidade = 0
for i in range(10):
    numero = (input(f"Diga o seu {i+1}° numero: "))
    while not numero.isnumeric():
        numero = (input(f"Diga o seu {i+1}° numero: "))
    numero = int(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f"São {pares} pares e {impares} impares!")

#Exercicio 3
soma = 0
for i in range(1,101):
    soma += i
print(soma)

#Exercicio 4
for i in range(1,11):
    print(f"Tabuada do {i}: ")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()

#LISTA!
lista = [6,True,'sadksada',[],4.2]

for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")

for elem in lista:
    print(elem)

adicionar = input("coloque algo na lista: ")
lista = []
lista.append(adicionar)
print(lista)
lista.append(111)
print(lista)
lista.append(11)
print(lista)
'''

LISTA USANDO LISTA 

#Exercicio 1
lista = [3,4,6,23,6,84,7,43,2,10]
soma = 0
for i in range(len(lista)):
    soma += lista[i]
print(f"soma = {soma} e media = {soma/len(lista)}")

#Exercicio 2
lista = [3,4,6,23,6,84,7,43,2,10]
pares = []
impares = []
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
        continue
    impares.append(lista[i])
print(f"pares = {pares} e impares = {impares}")

