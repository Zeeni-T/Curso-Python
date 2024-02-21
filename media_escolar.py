# Programa de Média
# Desenvolvido por Rafael

print("--------------------------------------")
print("            Media Escolar             ")
print("--------------------------------------")

# Criação das Variáveis
nome= ""
nota_bimestre_1 = 0.0
nota_bimestre_2 = 0.0
nota_bimestre_3 = 0.0
nota_bimestre_4 = 0.0
media = 0.0

# Entrada dos Dados
nome = input("Digite o nome do Aluno: ")
nota_bimestre_1 = float(input("Digite a sua Nota do 1 Bimestre: "))
nota_bimestre_2 = float(input("Digite a sua Nota do 2 Bimestre: "))
nota_bimestre_3 = float(input("Digite a sua Nota do 3 Bimestre: "))
nota_bimestre_4 = float(input("Digite a sua Nota do 4 Bimestre: "))


# Processar os Valores para obter IMC
media = (nota_bimestre_1 + nota_bimestre_2 + nota_bimestre_3 + nota_bimestre_4)/4

# Resultado do Processameto
print ()
print("--------------------------------------")
print("              Resultado               ")
print("--------------------------------------")
print ("Nome: " + nome)
print ("Média: " + str (media)+ " Media Final")

# Resultado da Nota
print(" ")
print(" ")
if media >= 7:
    media = print(f"Parabéns {nome}, Você Passou!")

elif media < 5:
    media = print(f"Desculpe {nome}, Você Reprovou!")

else:
    media = print(f"Dedique-se {nome}, Você irá Recuperar!")
print(" ")
print("--------------------------------------")
print("         Fim do Processamento         ")
print("--------------------------------------")
