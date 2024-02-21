# PROGRAMA PARA CAUCULAR IMC
# DESENVOLVIDO POR CELSO

print("----------------------------------------")
print("           CALCULADORA DE IMC           ")
print("----------------------------------------")
print(" ")

# CRIAÇÃO DAS VARIÁVEIS
nome = ""
peso = 0
altura = 0.0
imc = 0.0
situacao = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o seu Nome: ")
peso = int(input("Digite o seu Peso: "))
altura = float(input("Digite a sua Altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC
imc = peso / altura ** 2

if imc < 18.5:
    print("Você está Abaixo do Peso")
elif imc >= 18.5:
    print("Você está com o Peso Normal")
elif imc >= 24.9:
    print("Você está com o SobrePeso")
elif imc >= 29.9:
    print("Você está com Obesidade Grau 1")
elif imc >= 34.9:
    print("Você está com Obesidade Grau 2")
else:
    print("Você está com Obesidade Mórbida")

# SAÍDA DO PROCESSAMENTO
print(" ")
print("----------------------------------------")
print("               RESULTADO                ")
print("----------------------------------------")
print(" ")
print("Nome: " + nome)
print("Peso: " + str(peso) + "Kg")
print("Altura: " + str(altura) + "m")
print("IMC: " + str(imc))
