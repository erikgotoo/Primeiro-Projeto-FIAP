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


AULA PYTHON FUNCAO!!!!!!!!!!!!
'''
#DOCS DA AULA: t.ly/8kdzS


#Funcao verificador de idade para votos

def voto(nome, idade):
    if idade >= 16 and idade < 18:
        print(f"Sim, a pessoa {nome} pode votar")
        return True
    elif idade >= 18:
        print(f"A pessoa {nome} precisa votar")
        return True
    else:
        print(f"Não, a pessoa {nome} nao pode votar")
        return False

a = voto("Lucas", 38)
print(f"a primeira resposta foi {a}")
b = voto("Maira", 13)
print(f"a segunda resposta foi {b}")
c = voto("Pedro", 17)
nome2 = input("Digite o seu nome: ")
idade2 = int(input("Digite a sua idade: "))
voto(nome2, idade2)

#Funcao calculador de idades

#from datetime import datetime
#agora = datetime.now()
#ano_atual = agora.year
ano_atual = 2024
nome = input("Diga o seu nome: ")
def calculadorDeIdade(ano):
    idade = ano_atual - ano
    print(f"{nome} a sua idade é {idade} anos!")
    return idade


ano = int(input("Diga o seu ano de nacimento: "))
calculadorDeIdade(ano)

#Funcao descobrir o maior numero

def maiorNumero(numeros):
    maiorNumero = numeros[0]
    for maior in numeros:
        if maior > maiorNumero:
            maiorNumero = maior
    print(f"O maior numero é {maiorNumero}")
    return maiorNumero

listaNumeros = maiorNumero([-1,-2,-3,30,60,70,20,25,45,20,-100])
'''


def add1min(hora,minuto):
    proxMinuto = minuto+1
    if hora == 23 and proxMinuto == 60:
        return "00:00"
    elif proxMinuto == 60:
        hora = hora+1
        return f"{hora}:00"
    elif proxMinuto < 10:
        return f"{hora}:0{proxMinuto}"
    elif hora > 23 or proxMinuto > 60:
        return f"Informações Inválidas"
    else:
        return f"{hora}:{proxMinuto}"

print(add1min(23,22))

def numeroValido(numero):
    while True:
        numero = input("Diga o seu numero POSITIVO: ")
        if not numero.isnumeric():
            continue
        numero = int(numero)
        return numero

numero = input("Diga o seu numero: ")


adicionar = input("coloque algo na lista: ")
lista = []
lista.append(adicionar)
print(lista)
lista.append(111)
print(lista)
lista.append(11)
print(lista)

'''
quantia = int(input("Coloque seu numero na lista: "))

listaNumeros = []

for i in range(quantia):
    numero = int(input(f"Diga o seu {i + 1}°: "))
    listaNumeros.append(numero)


def somar(listaNumeros):
    soma = 0
    for i in listaNumeros:
        soma += i
    return soma

print(somar(listaNumeros))

===============================================================================================
def checa_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

quantia = checa_numero("Digite a quantidade de numeros para adicionar na lista: ")
listaNumeros = []

for qnt in range(quantia):
    numero = checa_numero(f"Diga o seu {qnt + 1}°: ")
    listaNumeros.append(numero)

def somar(listaNumeros):
    soma = 0
    for elem in listaNumeros:
        soma += elem
    return soma

def verificaMaior(lista):
    maior = lista[0]
    for elem in lista:
        if elem > maior:
            maior = elem
    return maior

def verificaPares(lista_pares_impares):
    pares = []
    impares = []
    for elem in lista_pares_impares:
        if elem % 2 == 0:
            pares.append(elem)
        else:
            impares.append(elem)
    return f"Pares:{pares},Impares{impares}"

def verificaOrdem(lista_crescente):
    a = lista_crescente[0]
    for elem in lista_crescente:
        


print("A soma é:",somar(listaNumeros))
print("O maior numero digitado foi:",verificaMaior(listaNumeros))
print("Os numeros pares são:",verificaPares(listaNumeros))


















'''
def verifica_pares(lista_numeros):
    pares = []
    for elem in lista:
        if elem%2 == 0:
            pares.append(elem)
    return pares

lista = [2,4,1,83,239,3249,439,32,43,54]
lista2 = [12,13,354,3435,213,2332,3432]

filtro_pares = verifica_pares(lista)
filtro_pares = verifica_pares(lista2)

print(filtro_pares)
print(filtro_pares)


#numero_real = checa_numero("Diga o seu numero: ")
#print(numero_real)
#x = checa_numero("Diga o seu numero: ")
#print(x)

def verifica_elemento(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
        return False

def forca_opcao(msg, lista_opcoes):
    opcao = input(msg)
    while not verifica_elemento((lista_opcoes,opcao)):
        print("Digite uma opção valida: ")
        opcao = int(opcao)
    return opcao

carros = ["up","gol","uno","celta"]
carros = forca_opcao("Qual carro vc deseja:\n ","Opcao invalida",carros)
print(carros)
continuar_ou_nao = forca_opcao("Deseja continuar: ","(s/n)",["s","n"])
print(continuar_ou_nao)
'''

============================================================================================
def checa_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero

quantia = checa_numero("Digite a quantidade de numeros para adicionar na lista: ")
listaNumeros = []

for qnt in range(quantia):
    numero = checa_numero(f"Diga o seu {qnt + 1}°: ")
    listaNumeros.append(numero)

def somar(listaSoma):
    soma = 0
    for elem in listaSoma:
        soma += elem
    return soma

def media(listaMedia):
    soma = somar(listaNumeros)
    media = soma/len(listaMedia)
    return media

def verificaMaior(listaMaior):
    maior = listaMaior[0]
    for elem in listaMaior:
        if elem > maior:
            maior = elem
    return maior

def verificaPares(lista_pares_impares):
    pares = []
    impares = []
    for elem in lista_pares_impares:
        if elem % 2 == 0:
            pares.append(elem)
        else:
            impares.append(elem)
    return f"Pares:{pares},Impares{impares}"

print("A soma é:",somar(listaNumeros))
print("A media é:",media((listaNumeros)))
print("O maior numero digitado foi:",verificaMaior(listaNumeros))
print("Os numeros pares são:",verificaPares(listaNumeros))

#----------------------------------------------------------------------
def inverteLista(lista):
    for i in range(len(lista)//2):
        ultimo = len(lista) - 1
        coringa = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = coringa
    return
                                                                        
lista = [1,2,3,4,5,6,7,8,9]

inverteLista(lista)
listaOriginal = lista[:]
inverteLista(listaOriginal)
print("Lista Original:",listaOriginal)
print("A lista invertida ficaria:",lista)



x = 2
print("CERTO") if x == 2 else print("ERRADO")

opcao = input("Diga uma das opções a ou b:").lower()

match opcao:
    case "a":
        print("Opção A selecionada")
    case "b":
        print("Opção B selecionada")
    case _:
        print("Opção Invalida")


'''
palavra = "banana"
myit = iter(palavra)

for i in palavra:
    print(next(myit))

aluno1 = "WELDER"
aluno2 = "ALEXIA"
aluno3 = "EDUDU"
aluno4 = "ABDINEY"

nome = aluno2

if nome in ["WELDER", "EDUDU, ABDINEY"]:
    print("MASCULINA")

else:
    print("FEMININO")

for i in range(0,30):
    if i == 15:
        print("ACHEI")
        break
else:
    print("NAO ACHEI")


Lista = ["Banana", "Abacaxi", "Manga", "Uva"]

for i, fruta in enumerate(Lista):
    print(i , ":", fruta)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a,b)
print(list(x))

names = ["John", "Marcelo"]
surnames = ["Smith", "Oka"]
numbers = [1, 2]

for name, surnames, numbers in zip(names, surnames, numbers):
    print(name, surnames, numbers)

quadrados = [i**2 for i in range(0, 101) if i <= 10]

print(quadrados)

def gerar_lista_de_quadrados():
    Lista = []
    for i in range(0, 101):
        Lista.append(i**2)
    return Lista

L = [i**2 for i in range(0, 101)]
print(L)
'''
import random

numero = random.randint(0,10)

while True:
    chute = int(input("Digite um chute: "))
    if chute == numero:
        print("Acertou Miserave")
        break
    else:
        print("ERRRRRRROU")
