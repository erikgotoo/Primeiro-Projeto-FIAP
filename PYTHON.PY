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
