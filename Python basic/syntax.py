n = -3 #int
pi= 3.14 #float
q='python' #string
print()
print(n,pi,q)
###########################################
idade=int(input('Digite sua idade:'))
print('Sua idade é', idade)
print(f'A divisão de -3.14/3 é: {pi/n}')
y=pi/n
print(round(y,3)) #apenas 3 casas depois da virgula
print()
###########################################
maiuscula=q.upper() #Todas maisc
minuscula=q.lower() #Todas minus
capital=q.capitalize() # So a 1º maisc
metade=q[0:4]
ultimas=q[4:]
w=q.replace('py','co')
print(maiuscula, minuscula, capital, metade,ultimas,w) 
print()
###########################################
r=' teste   '
t=r.strip() #retira espaços antes e dps
print(len(r),t, len(t))
print()
###########################################
a=True
b=False
print(a,b)
print(a & b) #&=and
print(a | b) #|=or
print(not a, not b)
print()
###########################################
print(7>2, 7<2, 7>=2, 7==7, 7!=2)
print()
###########################################
if 5>6:
    print('5 é maior que 6')
else:
    print('5 é menor que 6')
print()
###########################################
i = int(input('Digite um valor entre 0 e 5:'))
if i >= 0 and i <= 5: #0 < i < 5
    if i == 4:
        print('i é igual a 4')
    elif i == 3:
        print('i é igual a 3')
    else:
        print('i não é igual a 3 nem 4')
else:
    print('Digito inválido')
print()
###########################################
soma=0
for numero in range(1, 6):
    soma = soma +numero
print(soma)
print()
###########################################
num= -1
while num <1 or num>10:
    num=int(input('Digite um numero de 1 a 10:'))
print()
###########################################
tupla=('nike', 'adidas', 'oakley')
print(tupla)
print(tupla[2])
print(tupla.index('nike'))
for marca in tupla:
    print(marca)
print()
###########################################
l1=['verde','azul','amarelo'] #listas
l2=['branco','laranja','roxo']
l3=l1+l2
print(f'l1={l1}, l2={l2} e l3={l3}')
print(l1[1])
print(l2[0:2])
l1.append('rosa')
print(l1)
l1.remove('amarelo')
print(l1)
print()
for item in l3:
    print(item)
print()
###########################################
coleta={'mosquito': 3, 'abelha': 5, 'vespa': 1} #dicionario
print(coleta['vespa'])
coleta['gato']=4
print(coleta)
del(coleta)['abelha']
print(coleta)
print(coleta.items()) #dicionario completo 
print(coleta.keys()) #dicionario so as ''
print(coleta.values()) #dicionario so os valores 
coleta2={'cachorro': 10,'tigre':7}
print(coleta2)
coleta.update(coleta2) #juntar os 2 dicionarios
print(coleta)
print()
for animais, quantidade in coleta.items():
    print(f'Animal: {animais}, numero:{quantidade}')
print()
###########################################
biomoleculas=('proteina', 'carboidratos', 'acidos nucleicos', 'lipideos', 'carboidratos', 'acidos nucleicos', 'carboidratos') #Conjuntos(set)
print(biomoleculas)
print(set(biomoleculas)) #Retira os itens repetidos
c1={1,2,3,4,5}
c2={3,4,5,6,7}
c3=c1.intersection(c2)
print(c3)
print(c1.difference(c2))
print()
###########################################
import numpy as np #Matrizes
matriz=np.array([[2,3,1],[4,5,6]])
print(matriz)
print(matriz.shape) #linha x coluna
print(matriz[0]) #1º linha
print(matriz[1][1]) #linha 0 coluna 1
for i in range (matriz.shape[0]): #Percorre as linas
    print(matriz[i])
    for j in range(matriz.shape[1]): #Percorre as colunas
        print(matriz[i][j])
print()
###########################################
def soma(a,b):
    print(a+b)
soma(2,3)

def sub (a,b):
    return (a-b)
r=sub(10,7)
print(r)

def epg (m, h, g=10):
    '''Calcula a energia potencial gravitacional
    m=massa, h=altura, g= acdeleração da gravidade, com valor default de 10'''
    e=m*g*h
    return e
print(epg(12,2))
help(epg)
print()
###########################################
import math
print(math.sqrt(9))
print(math.cos(45))
print(math.log(20, 10)) # Quando nao passa a base, a função utiliza o número de euler
print(math.e)
print()
###########################################
import datetime
print(dir(datetime)) #Ver os recursos da biblioteca
print(datetime.datetime.today())
print(datetime.datetime.now())
print()
import random
print(random.random()) #Gera nº aleatorios entre 0 e 1
print(random.randint(1, 10)) #Gera nº aleatorios entre 1 e 10
x=['j', 88, '9-i', 'XZ']
print(random.choice(x)) # Aleatorio da lista x
print()
###########################################
import time as tm 
tm.time() #Quanto tempo o codigo levou para executar
antes =tm.time()

lista = []
for i in range(0,10000):
    lista.append(i)
depois = tm.time()

intervalo = depois - antes
print(f'Tempo de execução: {intervalo} segundos')
print()

print('Finalizando') #Mandar msg para o usuario
tm.sleep(2)
print('...')
tm.sleep(2)
print('Obrigado')
print()
###########################################
#Tratamento de erros
'''NameError: variável nao foi definida 
TypeError: tipos de dados incompatíveis
RuntimeError: erro de execução
SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
ZeroDivisionError: divisão por zero
IndexError: índice está fora da coleção'''

while True:
    try: #Não mostra msg de erro e sim uma msg personalidaza
        nn=int(input('Digite um numero inteiro:'))
    except:
        print('Valor inválido')
    else:
        print(f'O valor digitado é {nn}')
        break
print()

lista_ex = []
try:
    print('Divisão entre 2 numeros')
    lista_ex.append(float(input('Digite o primeiro valor:')))
    lista_ex.append(float(input('Digite o segundo valor:')))
    divisao = lista_ex[0]/lista_ex[1]
except ValueError:
    print('Erro! Valor inválido')
except ZeroDivisionError:
    print('Erro! Divisão por zero')
except IndexError:
    print('Erro! Incdice Invalido')
except KeyboardInterrupt:
    print('Usuario interrompeu a execução')
else:
    print(f'O resultado da divisão é {divisao}')
print()
###########################################
with open('teste_txt.txt') as txt:
    for linha in txt:
        print(linha)
print()
###########################################
import re #Expressões regulares
frase = 'Olá, meu número de telefone é (42)00010-0000'
print(re.search('\(\d{2}\)\d{4,5}-\d{4}', frase))
frase = 'A placa de carro que eu anotei durante o acidente foi FrT-1998'
print(re.search('[A-Za-z]{3}-\d{4}', frase))
email = 'Entre em contato, meu email é teste@teste.com'
print(re.search('\w+@\w+\.com', email))
print()

frase2 = 'Meu número de telefone atual é (42)0000-0000. O número (56)1111-1111 é o antigo'
print(re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase2))
print()

emails = '''Nome: Teste 1
email: teste1@teste.com
Nome: Teste 2
email: teste2@teste.com
Nome: Teste 3
email: teste3@teste.com.br
'''
print(re.findall('\w+@\w+\.\w*', emails))
print()
###########################################
class Triangulo:
  def __init__(self, lado1, lado2, lado3, base, altura):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
    self.base = base
    self.altura = altura
  
  def area(self):
    return (self.base * self.altura) / 2

  def tipo(self):
    if self.lado1 > self.lado2 + self.lado3:
      return 'não é um triângulo'
    elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
      return 'triângulo isósceles'
    else:
      return 'outro tipo de triângulo'

t1 = Triangulo(5, 1, 3, 4, 3)
print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)
print(t1.area())
print(t1.tipo())
print()
###########################################
class Aluno:
  def __init__(self, nome, nota1, nota2):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media = 0.0
   
  def calcula_media(self):
    self.media = (self.nota1 + self.nota2) / 2
    return self.media

  def mostra_dados(self):
    print('Nome: ', self.nome)
    print('Nota 1:', self.nota1)
    print('Nota 2:', self.nota2)
    print('Média:', self.media)
  
  def resultado(self):
    if self.media >= 6.0:
      print('Aprovado')
    else:
      print('Reprovado')

aluno1 = Aluno('Pedro', 7.0, 9.0)
media = aluno1.calcula_media()
print(media)
aluno1.mostra_dados()
aluno1.resultado()
print()
###########################################
