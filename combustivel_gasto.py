print("-------------------------------------------------")
print("       consumo de combustível       ")
print("-------------------------------------------------")

modelo_do_carro = " "
autonomia_do_carro = 0
distancia_da_viagem = 0
preco_do_combustivel = 0.0

modelo_do_carro = input("Modelo do carro? ")
autonomia_do_carro = int(input("Autonomia do carro? "))
distancia_da_viagem = int(input("Distância da viagem? "))
preco_do_combustivel = float(input("Preço do combustível? "))

quantidade_de_combustivel_utilizado = distancia_da_viagem / autonomia_do_carro
total_gasto_com_a_viagem = (distancia_da_viagem / autonomia_do_carro) * preco_do_combustivel

print("-------------------------------------------------")
print("                  r e s u l t a d o                 ")
print("-------------------------------------------------")
print(" ")
print(f"Modelo do veículo: {modelo_do_carro}")
print(f"Autonomia do veículo: {autonomia_do_carro} Km/1")
print(f"Distância percorrida: {distancia_da_viagem} Km")
print(f"Valor do combustível: R$ {preco_do_combustivel}")
print(" ")
print("-------------------------------------------------")
print(f"Quantidade de combustível utilizado: {quantidade_de_combustivel_utilizado} 1")
print(f"Total gasto com a viagem: R$ {total_gasto_com_a_viagem}")
print("-------------------------------------------------")
