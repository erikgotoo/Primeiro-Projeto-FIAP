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
