# ===============================
# Atividade Prática 01
# ===============================

# Programa 1: Saudação
print("Hello, world!")

# Programa 2: Calculadora de Soma
numero1 = 12
numero2 = 14
soma = numero1 + numero2
print("A soma é:", soma)

# Programa 3: Calculadora de Volume
comprimento = 12
largura = 14
altura = 20
volume = comprimento * largura * altura
print("O volume da caixa é:", volume, "cm³")

# Programa 4: Calculadora de Preço Total
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3
preco_total = preco_unitario * quantidade

print("Produto:", nome_produto)
print("Preço unitário: R$", preco_unitario)
print("Quantidade:", quantidade)
print("Preço total: R$", preco_total)

# Programa 5: Diferença de Produtos
A = int(input())
B = int(input())
C = int(input())
D = int(input())

DIFERENCA = (A * B - C * D)
print("DIFERENCA =", DIFERENCA)

# ===============================
# Atividade Prática 02
# ===============================

# Programa 1: Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("R$", valor_reais, "equivale a:")
print("US$", round(valor_dolar, 2))
print("€", round(valor_euro, 2))

# Programa 2: Calculadora de Desconto
nome_produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * (desconto_percentual / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", desconto_percentual, "%")
print("Valor do desconto: R$", valor_desconto)
print("Preço final: R$", preco_final)

# Programa 3: Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print("Notas do aluno:")
print("Nota 1:", nota1)
print("Nota 2:", nota2)
print("Nota 3:", nota3)
print("Média final:", round(media, 2))

# Programa 4: Calculadora de Consumo de Combustível
distancia = 300
combustivel = 25

consumo_medio = distancia / combustivel

print("Distância percorrida:", distancia, "km")
print("Combustível gasto:", combustivel, "litros")
print("Consumo médio:", round(consumo_medio, 2), "km/l")

# Programa 5: Calculadora de Soma com Entrada do Usuário
A = int(input())
B = int(input())

X = A + B

print("X =", X)

# Programa 6: Calculadora de Salário por Horas Trabalhadas
numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

salario = horas_trabalhadas * valor_por_hora

print("NUMBER =", numero_funcionario)
print("SALARY = R$", format(salario, ".2f"))

# ===============================
# Atividade Prática 03
# ===============================

# Programa 1: Área da Circunferência
raio = float(input())
PI = 3.14159265
area = PI * (raio ** 2)
print(f"A={area:.4f}")

# Programa 2: Classificador de Idade
idade = int(input("Digite a idade: "))
if 0 <= idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# Programa 3: Calculadora de IMC
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obeso")

# Programa 4: Conversor de Temperatura
temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()
resultado = temp

if origem == 'C':
    if destino == 'F':
        resultado = (temp * 9/5) + 32
    elif destino == 'K':
        resultado = temp + 273.15
elif origem == 'F':
    if destino == 'C':
        resultado = (temp - 32) * 5/9
    elif destino == 'K':
        resultado = (temp - 32) * 5/9 + 273.15
elif origem == 'K':
    if destino == 'C':
        resultado = temp - 273.15
    elif destino == 'F':
        resultado = (temp - 273.15) * 9/5 + 32
else:
    print("Unidade de origem inválida")
    exit()

print(f"Temperatura convertida: {resultado:.2f}")

# Programa 5: Verificador de Ano Bissexto
ano = int(input("Digite o ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é ano bissexto")

# Programa 6: Calculadora de Comissão
nome = input()
salario_fixo = float(input())
total_vendas = float(input())

total_receber = salario_fixo + (total_vendas * 0.15)
print(f"TOTAL = R$ {total_receber:.2f}")

# Programa 7: Calculadora da Média com Exame
N1, N2, N3, N4 = map(float, input().split())
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f"Média: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    media_final = (media + exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Média final: {media_final:.1f}")

# ===============================
# Atividade Prática 04
# ===============================

# Programa 1: Calculadora com Tratamento de Erros
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            print("Operação inválida! Tente novamente.")
            continue

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero!")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}")
        break

    except ValueError:
        print("Entrada inválida! Por favor, insira números válidos.")

# Programa 2: Registro de Notas com Cálculo de Média
notas = []

while True:
    entrada = input("Digite uma nota de 0 a 10 ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite um número entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")

# Programa 3: Verificação de Senha Forte
while True:
    senha = input("Digite uma senha forte ou 'sair' para encerrar: ")

    if senha.lower() == 'sair':
        print("Encerrando verificação.")
        break

    if len(senha) < 8:
        print("Senha fraca: deve ter pelo menos 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte cadastrada com sucesso!")
    break

# Programa 4: Verificador de Números Pares e Ímpares
pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("O número é par.")
            pares += 1
        else:
            print("O número é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: entrada inválida. Por favor, insira um número inteiro.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

# ===============================
# Atividade Prática 05
# ===============================

# Programa 1: Função que Calcula a Gorjeta
def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

valor = float(input("Valor total da conta: "))
porcentagem = float(input("Porcentagem da gorjeta: "))
print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")

# Programa 2: Função que Verifica se é Palíndromo
def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")
print("Sim" if eh_palindromo(frase) else "Não")

# Programa 3: Calcula Preço Final com Desconto
preco = float(input("Preço do produto: "))
desconto = float(input("Percentual de desconto: "))
preco_final = preco - (preco * desconto / 100)
print(f"Preço final: R$ {preco_final:.2f}")

# Programa 4: Função que Calcula Idade em Dias
from datetime import date

def idade_em_dias(ano_nascimento):
    return (date.today().year - ano_nascimento) * 365

ano = int(input("Ano de nascimento: "))
print(f"Idade aproximada em dias: {idade_em_dias(ano)} dias")


# Atividade 6 - Programa 1: Gerar senha aleatória
import random
import string

tamanho = int(input("Quantidade de caracteres da senha: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
print("Senha gerada:", senha)


# Atividade 6 - Programa 2: Gerar perfil de usuário aleatório usando API
import requests

resposta = requests.get('https://randomuser.me/api/')
dados = resposta.json()
usuario = dados['results'][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario['email']
pais = usuario['location']['country']

print("\nPerfil de usuário aleatório:")
print("Nome:", nome)
print("Email:", email)
print("País:", pais)


# Atividade 6 - Programa 3: Consultar endereço pelo CEP usando API ViaCEP
cep = input("\nInforme o CEP: ").replace('-', '').strip()
url = f"https://viacep.com.br/ws/{cep}/json/"
resposta = requests.get(url)
dados = resposta.json()

if 'erro' not in dados:
    print("Logradouro:", dados['logradouro'])
    print("Bairro:", dados['bairro'])
    print("Cidade:", dados['localidade'])
    print("Estado:", dados['uf'])
else:
    print("CEP inválido.")


# Atividade 6 - Programa 4: Consultar cotação de moeda usando API AwesomeAPI
moeda = input("\nInforme o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
resposta = requests.get(url)
dados = resposta.json()
chave = moeda + 'BRL'

if chave in dados:
    cotacao = dados[chave]
    print("Valor atual:", cotacao['bid'])
    print("Valor máximo:", cotacao['high'])
    print("Valor mínimo:", cotacao['low'])
    print("Data e hora da última atualização:", cotacao['create_date'])
else:
    print("Código de moeda inválido ou não encontrado.")

# Atividade 7 - Programa 1: Ler arquivo de log e calcular média e desvio padrão
import statistics

tempos = []
# Certifique-se de que o arquivo 'log_treinamento.txt' existe no mesmo diretório
# com alguns números, um por linha.
# Exemplo de conteúdo para 'log_treinamento.txt':
# 10.5
# 11.2
# 10.8
try:
    with open('log_treinamento.txt', 'r') as arquivo:
        for linha in arquivo:
            try:
                tempo = float(linha.strip())
                tempos.append(tempo)
            except ValueError:
                pass

    if tempos:
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0
        print("Média do tempo de execução:", media)
        print("Desvio padrão:", desvio)
    else:
        print("Nenhum dado válido encontrado no arquivo de log.")
except FileNotFoundError:
    print("Arquivo 'log_treinamento.txt' não encontrado.")


# Atividade 7 - Programa 2: Escrever dados em um arquivo CSV
import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Maria", 22, "Belo Horizonte"]
]

with open('dados_pessoais.csv', 'w', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)

print("\nArquivo CSV criado com sucesso.")

#Atividade Prática 08

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report

data = load_breast_cancer()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]  

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)

print("=== Métricas de Classificação ===")
print(f"Precisão: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
print(f"AUC-ROC: {auc:.4f}")
print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))
print("\n=== Matriz de Confusão ===")
print(confusion_matrix(y_test, y_pred))