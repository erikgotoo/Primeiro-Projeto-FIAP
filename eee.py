Olá,
aprendendo a usar o git
27/02/2024

Mudanças feitas pelo proprio app GITHUB 👍

PRIMEIROS PASSOS: PYTON 
'''
frase = "Hello World!"
primeiro_numero = 1
segundo_numero = 1.5
booleana = False
print(frase)
print(type(frase))
print(primeiro_numero)
print(type(primeiro_numero))
print(segundo_numero)
print(type(segundo_numero))
print(booleana)
print(type(booleana))
'''
'''
primeiro_numero = 2
segundo_numero = 3
soma = primeiro_numero + segundo_numero
print (f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")
'''
'''
primeiro_numero = 2
segundo_numero = 3
multiplicação = primeiro_numero * segundo_numero
print (f"A multiplicação entre {primeiro_numero} e {segundo_numero} é {multiplicação}")
divisao = primeiro_numero / segundo_numero
print (f"A divisao entre {primeiro_numero} e {segundo_numero} é {divisao}")

nome = (input("Diga seu nome : "))
print(f"Seja Bem Vindo, {nome}")
primeiro_numero = int(input("Diga um numero : "))
segundo_numero = int(input("Diga outro numero : "))
soma = primeiro_numero + segundo_numero
print(f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")
subtracao = primeiro_numero - segundo_numero
print(f"A subtracao entre {primeiro_numero} e {segundo_numero} é {subtracao}")
multiplicação = primeiro_numero * segundo_numero
print (f"A multiplicação entre {primeiro_numero} e {segundo_numero} é {multiplicação}")
divisao = primeiro_numero / segundo_numero
print (f"A divisao entre {primeiro_numero} e {segundo_numero} é {divisao}")

frase = "Hello"
frase = frase + " World,"
frase = frase + " Como você esta?"
print (frase)
frase = "Estou bem"
frase = frase + " Qual o seu nome?"
print(frase)
nome = int(input("Diga o seu nome : "))

a = 3
b = 5
aux = a 
a = b 
b = aux
print (a)
print (b)
'''
a = 3>4
b = 2!=3
c = not 5==6
d = 'texto' in 'Em linguística, a noção de texto é ampla e ainda aberta a uma definição mais precisa. Grosso modo, pode ser entendido como manifestação linguística das ideias de um autor, que serão interpretadas pelo leitor de acordo com seus conhecimentos linguísticos e culturais. Seu tamanho é variável.'
e = 2>1 or 8>9
print (a)
print(b)
print (c)
print (d)
print (e)


FRONT-END
!DOCTYPE html>
<html lang="pt-bt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aula 01 - Web</title>
</head>
<body>
 
    <!-- Tipos de Cabeçalhos -->
    <h1>Aula de Web</h1> 
    <h2>Aula de Web</h2> 
    <h3>Aula de Web</h3> 
    <h4>Aula de Web</h4> 
    <h5>Aula de Web</h5> 
    <h6>Aula de Web</h6> 

    <!-- parágrafos: -->
    <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur natus, vitae commodi qui voluptatum quaerat nihil accusantium! Quia hic, tempora ratione dolor aliquam similique voluptatum iure repudiandae, odit repellat minus.
    </p>
    
    <!-- Imagens -->
    <figure>
       <img src="./Images/pexels-layanne-17189429 (1).jpg" alt="Estadio do Atletico Mineiro.">

       <img src="Images/pexels-thiago-japyassu-20450299 (1).jpg" alt="Pão de Queijo.">

       <figcaption>Fotos retiradas do 
       <a href="https://www.pexels.com/pt-br/" target="_blank">Pexels</a> 
       </figcaption>
    </figure>
    
     <video src="./videos/pexels-juancarlos-córdova-5854603.mp4" controls muted autoplay loop></video>
    
</body>
</html>

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

AULA 3 PYTHON: 
'''
letra = input("Diga uma letra:")
if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
   print(F"{letra} é uma Vogal")
else:
   print(F"{letra} é uma Consoante")

nota = int(input("Diga sua nota:"))
if nota >= 6:
    print("Aprovado!")
elif nota < 6 and nota >= 4 :
    print("Exame")
else:
    print("Reprovado!")

#Imposto de renda;
salario = int(input("Diga seu salario:"))
if(salario <= 1903.98):
  print ("Você está isento do Imposto")
elif (salario <= 2826.65):
  imposto = salario * 0.075
  print(f"Você deve pagar {imposto} de Imposto, você receberá: {salario - imposto}")
elif (salario <= 3751.05):
  imposto = salario * 0.15
  print(f"Você deve pagar {imposto} de Imposto, você receberá: {salario - imposto}")
elif (salario <= 4664.68):
  imposto = salario * 0.225
  print(f"Você deve pagar {imposto} de Imposto, você receberá: {salario - imposto}")
else:
  imposto = salario * 0.275
  print(f"Você deve pagar {imposto} de Imposto, você receberá: {salario - imposto}")

#MELHOR ESTILO PRA FAZER ISSO^^
salario = int(input("Diga seu salario:"))
if(salario <= 1903.98):
    aliquota = 0
elif (salario <= 2826.65):
    aliquota = 7.5/100
elif (salario <= 3751.05):
    aliquota = 15/100
elif (salario <= 4664.68):
    aliquota = 22.5/100
else:
    aliquota = 27.5/100
desconto = aliquota*salario
salario = salario - desconto
print(f"Seu salario apos o desconto de {desconto} será de R${salario:.2f}")
#Exercicio 1
pn = int(input("Diga o primeiro número:"))
sn = int(input("Diga o segundo número:"))
conta = pn > sn
if (conta):
    print (f"{pn} é maior que o {sn}")
else:
    print (f"{sn} é maior que o {pn}")

#Exercício 2
ano = int(input("Diga seu ano de nascimento: "))
if ano < 2006:
    print("Você pode votar!")
else:
    print("Você nâo pode votar esse ano!")

#Exercicío 3
senha = int(input("Diga a sua senha:"))
if senha == 1234:
  print("Acesso Permitido!")
else:
  print("Acesso Negado!")

#Exercicío 4
quantidade = int(input("Diga a quantidade de maça:"))
if quantidade < 12:
    print(f"O valor a ser pago é {quantidade * 0.30} reais")
else:
    print(f"O valor a ser pago é {quantidade * 0.25} reais")

#Exercicio 5:
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite outro número: "))
if a > b and a > c:
    aux = a
    a = c
    c = aux #Inverte a com c, caso a seja maior
elif b > c:
    aux = b
    b = c
    c = aux #Inverte b com c, caso b seja maior
if a > b:
    aux = a
    a = b
    b = aux #Inverte a com b, caso a seja maior
print(a,b,c)
'''


#Exercicio 6
sexo = int(input("Digite 1 (Homem) e 2 (Mulher), diga o seu genero:"))
altura = float(input("Diga o seu altura:"))
formulah = (72.7*altura)-58
formulam = (62.1*altura)-44.7
if sexo == 1:
    print(f"O seu peso ideal é de {formulah}")
else:
    print(f"O seu peso ideal é de {formulam}")
'''

#Exercício 7 e 8

lados = int(input("Digite o número de lados do polígono: "))
forma = ''
if(lados < 3):
    print(f"Não é um polígono")
elif (lados > 5):
    print("Polígono não identificado")
else:
 tamanho = int(input("Digite o tamanho dos lados do polígono: "))
if(lados == 3):
    forma = 'triangulo'
elif(lados == 4):
    forma = 'quadrado'
elif(lados == 5):
   forma = 'pentagono'
   perimetro = lados*tamanho
if forma:
    print(f"Você escolheu um {forma} com o perimetro de {perimetro}")
'''

#Exercício 9
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))
if(numero1 > numero2 and numero1 > numero3):
    print(f"O maior número é {numero1}")
elif(numero2 > numero3):
    print(f"O maior número é {numero2}")
else:
    print(f"O maior número é {numero3}")

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
numero3 = int(input("Digite outro número: "))
maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3
print(maior)

'''
#Exercício 10
lado1 = int(input("Digite o tamanho do primeiro lado: "))
lado2 = int(input("Digite o tamanho do segundo lado: "))
lado3 = int(input("Digite o tamanho do terceiro lado: "))
if(lado1 == lado2 and lado1 == lado3):
    print(f"O triângulo é equilátero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print(f"O triângulo é isósceles")
else:
    print(f"O triângulo é escaleno")
'''

#Exercício 11
angulo1 = int(input("Digite o primeiro ângulo: "))
angulo2 = int(input("Digite o segundo ângulo: "))
angulo3 = int(input("Digite o terceiro ângulo: "))
if (angulo1 == 90 or angulo2 == 90 or angulo3 == 90):
  print("O triângulo é retângulo")
elif (angulo1 > 90 or angulo2 > 90 or angulo3 > 90):
  print("O triângulo é obtusângulo")
else:
  print("O triângulo é acutângulo")

FRONT AULA 2 

body{ background-color: beige ;
      font-family: "Quicksand", sans-serif;
}

h1 {
   color: #9a158f;
   font-size: 50px;
   text-align: center;
  }

  p {color: black;
    font-size: 16px;
    line-height: 1.5;
    font-weight: 300;
    
}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formatação CSS</title>
    <!--Chamada do Google Fonts-->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&family=Rubik+Puddles&display=swap" rel="stylesheet"> 
    <!-- Chamada CSS -->
    <link href="./CSS/style.css" rel="stylesheet" />
</head>
<body>
    
    <!--<conteiner que recebe qualquer conteúdo -->
   <div>
    <h1>Formação CSS</h1>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ex vero possimus eos aut quisquam, sequi error numquam, similique quod maxime inventore nobis labore sed vitae iusto vel quaerat. Fugiat, nihil?


        "Saudades do Eric🧙‍♂️" 
    </p>
    <a href="https://www.lipsum.com/" target="_blank">Mais Informações</a>


   </div>
    

</body>
</html>

AULA 4 PYTHON

'''
#Exercicio 8 (outro metodo)
lados = int(input("Digite o número de lados do polígono: "))
forma = ''
if(lados < 3):
    print(f"Não é um polígono")
elif (lados > 5):
    print("Polígono não identificado")
else:
if(lados == 3):
    forma = 'triangulo'
elif(lados == 4):
    forma = 'quadrado'
else:
    forma = "Pentagono"
medida = int(input("Diga a medida do lado:"))
perimetro = lados*medida
print(f"O seu poligono é {forma}, e o perimetro é {perimetro}")

#Multa
velocidade = int(input("Insira a sua velocidade:"))
if velocidade <= 100:
    print(f"Você esta isento da multa!")
else:
  if velocidade <= 120:
    conta = 0.20*velocidade
  elif velocidade <= 150:
    conta = 0.20*120+0.30*velocidade
  else:
    conta = 0.20*120+0.30*150+0.40*velocidade
    print(F"Você estava a {velocidade} e deve pagar {conta:.2f} de multa!")

#Descobrir par ou impar
numero = int(input("Diga o seu numero: "))
if numero%2 == 0:
    print(f"{numero} é par pois {numero} % {2}= {numero%2}")
else:
    print(f"{numero} é impor pois {numero} % {2}= {numero%2}")

#Comparador de quantos pares e quantos impares"
numero1 = int(input("Diga o primeiro numero: "))
numero2 = int(input("Diga o segundo numero: "))
numero3 = int(input("Diga o terceiro numero: "))
numero4 = int(input("Diga o quarto numero: "))
numero5 = int(input("Diga o quinto numero: "))

par = 0
par = numero1%2
par = par + numero2%2
par = par + numero3%2
par = par + numero4%2
par = par + numero5%2
impar = 5 - par

print(f"São {par} numeros pares e {impar} numeros impares")
'''
AULA 5 PYTHON
'''
par = 0
quantidade = 0
while quantidade < 10:
  numero = int(input("Diga um numero: "))
  if numero%2 == 0:
    par = par + 1 #par+= 1 (simplificado)
  quantidade += 1
print(F"Você digitou {par} pares e {10-par} impares.")

senha = int(input("Digite a sua senha: "))
while senha != 9090:
     print("Você errou burro, digite novamente!")
     senha = int(input("Digite a sua senha: "))
print("Você acertou sua senha")

senha = int(input("Digite a sua senha: "))
testes = 1
senha1 = 9090
while senha != senha1 and testes < 3:
     print(f"Você errou burro, mais {3 - testes} tentativas!")
     senha = int(input("Digite a sua senha: "))
     testes += 1
if senha == senha1:
     print("Você acertou sua senha")
else:
     print("Limite de senha atingida!")

numero = int(input("Digite o seu numero: "))
mais = 0
while numero != 0:
    mais += numero
    numero -= 1
print(mais)

#MELHOR JEITO FAZER
numero = int(input("Digite o seu numero: "))
i = 0
soma = 0
while i < numero:
    i += 1
    soma += i
    print(soma)
'''
front css

<-- link css  -->
     <link rel="stylesheet" href="./css/styless.css">
*{
 margin: 0;
 padding: 0%;
 box-sizing: border-box;





}



.conteiner{ 
 width: 100%;
 height: 100vh;
 /* background-color: rgb(90, 20, 61); */
 /* margin: 0px ; */
 /* border:20px solid goldenrod; */
 /* color: beige; */
 /* padding: 30px; */
 /* box-sizing: border-box; */

 background-image: url(../images-vinicola/vinicolas/pexels-alleksana-4186555.jpg) ;
 background-repeat: no-repeat;
 background-size: cover;
 background-position: 50%;

}

WEB DEV (AULA 1 JS)
INDEX.HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <h1></h1>
    <script src="/script.js"></script>
    
    
</body>
</html>
SCRIPT.JS
/*  
// dar um alerta para pessoas que entram no site 
alert("Hello World!")
// dar uma opçao de resposta para o usuario do site 
prompt("Digite seu nome: ")
// dar opçao de escolha para o usuario do site 
confirm("Você deseja sair? ")
// mostrar pro usuario no console do site
console.log("MINEIRO DÁ")

// criar variaveis
var nome = "Erik"
var idade = 20
var dataaula = "dia 02/04/2004"

console.log(nome)
console.log(idade)
console.log(dataaula)
*/
// usar prompt pra dar o nome e mostrar no console
var nome = prompt("Digite o seu nome: ")
var idade = prompt("Digite a sua idade: ")
var prof = prompt("Digite a sua profissao: ")
var titulo = document.querySelector("h1")
// usar informação coletada do nome pra usar em frases
console.log("Ola " + nome + ", seja bem-vindo, você tem " + idade + " anos e sua profissao é " + prof + ".")

titulo.innerHTML = "Ola " + nome + ", seja bem-vindo, você tem " + idade + " anos e sua profissao é " + prof + "."

AULA 6 PYTHON

'''
idoso = input("Voce é idoso? sim ou nao: ")
while not (idoso == "sim" or idoso == "nao"):
    print("Resposta errada!")
    idoso = input("Voce é idoso? sim ou nao: ")

if idoso == "sim":
     print("coisa ruim")
else:
      print("coisa boa")

numero = int(input("Digite o seu numero: "))
i = 0
soma = 0
while True:
    i += 1
    soma += i
    if i == numero:
        break
    print(soma)

idade = input("Diga sua idade: ")
while not idade.isnumeric():
    print("Digite um numero")
    idade = input("Diga sua idade: ")
idade = int(idade)
print(type(idade))
'''
numero = input("Diga seu numero: ")
while True:
    if numero.isnumeric():
      #if(0 <= int(numero) >= 100):
      if int(numero) > 0 and int(numero) < 100:
        numero = int(numero)
        break
        print("Numero invalido")
    print("Precisa ser numero")    
print("Numero de merda!")

AULA 7 PYTHON
nota = (input("Digite sua nota da prova: "))
while not nota.isnumeric():
    print("Coloque sua nota de 0 a 10")
    nota = (input("Digite sua nota da prova: "))
nota = int(nota)
if nota < 11:
 print(f"Nota {nota} de merda")
else:
    print("Nota impossivel burro, 10 é o limite!")
'''
nome = input("Diga o seu nome: ")

letrasnome = len(nome)
while letrasnome <= 3:
    nome = input("Diga o seu nome com no minimo 4 letras: ")
    letrasnome = len(nome)

idade = input("Diga a sua idade: ")

while not idade.isnumeric():
    if (int(idade) < 0 or (int(idade) > 150
     print("Diga a sua idade, vc nasce com 0 e morre com no max 150")

salario = (input("Diga o seu salario"))

while True:
 if salario.isnumeric():
     if int(salario) > 0:
         break
     print("Voce eh desempregado? Digite mais que 0")
 else:
  print("NUMERO ANIMAL!")

sexo = input("Diga o seu sexo em f para feminino e m para masculino: ")
while not (sexo == "f" or sexo == "m"):
    sexo = input("Diga o seu sexo em f para feminino e m para masculino: ")

estadocivil = input("Diga o seu estado civil em 's' solteiro,'c' casado,'v' viuvo,'d' divorciado")
while not (estadocivil == 's' or estadocivil == 'c' or estadocivil == 'v' or estadocivil == 'd'):
    estadocivil = input("Diga o seu estado civil em 's' solteiro,'c' casado,'v' viuvo,'d' divorciado")

    Aula Front 5
    :root {
    --color-light: #ffffff;
    --color-dark: #000000;
    --color-pink: #dc143d;
    --transition: .5s;
    --font-boddy: "Poppins", sans-serif;
}

* {
    margin: 0;
    /* padding: 0; */
    box-sizing: border-box;
    font-family: var(--font-boddy);
}

ul, ol {
    list-style: none;
}

a {
    text-decoration: none;
    color: var(--color-light);
    font-weight: 600;
    transition: .3s;
}

a:hover {
    color: var(--color-pink);
}

.container {
    width: 100%;
    height: 100vh;
    /* background-color: gray; */
    /* border: 10px solid var(--color-dark); */
    /* padding: 20px; */
    
    background-image: linear-gradient(to top, rgba(0, 0, 0, .8), rgba(0, 0, 0, .3));
    background-image: url(../images/images-vinicola/vinicolas/pexels-alleksana-4186555.jpg);
    background-repeat: no-repeat;
    background-size: cover; 
    background-position: 50%;
}

.header-page {
    width: 100%;
    height: 80px;
    /* background-color: blue; */
    display: flex;
    /* flex-direction: row-reverse; */
    padding: 0px 50px;
    align-items: center;
    justify-content: space-between;
}

.header-page ul {
    display: flex;
    gap: 30px;
} 




<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vinheria Agnello</title>

    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="./css/styles.css">
</head>
<body>
    <div class="container">
        <header class="header-page">
            <h1>Vinícula Agnello</h1>
            <!-- nav>ul>li*4>{Link$} -->
            <nav>
                <ul>
                    <li><a href="https://sudoku-online.com/pt" target="_blank">Link1</a></li>
                    <li><a href="">Link2</a></li>
                    <li><a href="">Link3</a></li>
                    <li><a href="">Link4</a></li>
                </ul>
            </nav>
        </header>
    </div>
</body>
</html>


AULA 7 PYTHON
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
quantidade = 0
impar = 0
par = 0
while quantidade < 10:
 numero = (input(f"Diga o seu {quantidade+1}° numero: "))
 if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        par += 1
    else:
       impar += 1
    quantidade += 1
print(f"São {par} pares e {impar} impares!")
'''
WEB DEV AULA 2 JS

function soma(){
    //Entrada
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    //Processamento
    var soma = n1 + n2
    //Saída
    resultado.innerText = `O resultado da soma é ${soma}`
}

function subtracao(){
    //Entrada
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    //Processamento
    var subtracao = n1 - n2
    //Saída
    resultado.innerText = `O resultado da subtração é ${subtracao}`
}

function divisao(){
//Entrada
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    //Processamento
    var divisao = n1 / n2
    //Saída
    resultado.innerText = `O resultado da divisão é ${divisao}`
    
if (n2 === 0 || isNaN(n2) ) {
    resultado.innerText = "Erro: divisâo por zero";
}
else {
    resultado.innerText = n1 / n2;
}

}

function multiplicacao(){
    //Entrada
    var n1 = parseFloat(document.getElementById("numero1").value);
    var n2 = parseFloat(document.getElementById("numero2").value);
    //Processamento
    var multiplicacao = n1 * n2
    //Saída
    resultado.innerText = `O resultado da multiplicação é ${multiplicacao}`
}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <div class="container"></div>
    <h1>Calculadora HTML + JS</h1>
    <label for="numero1">Numero1:</label>
    <input type="number" id="numero1" placeholder="Digite Aqui">
    <label for="numero2">Numero2:</label>
    <input type="number" id="numero2" placeholder="Digite Aqui">
    <button id="btnSoma" onclick="soma()">+</button>
    <button id="btnSubtracao" onclick="subtracao()">-</button>
    <button id="btnDivivsao" onclick="divisao()">/</button>
    <button id="btnMultiplicacao" onclick="multiplicacao()">*</button>
    <h2>Resultado:</h2>
    <p id="resultado"></p>


    <script src="script.js"></script>
</body>
</html>




