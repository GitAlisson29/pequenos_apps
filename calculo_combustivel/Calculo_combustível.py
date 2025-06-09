tempo = float(input("Digite o tempo gasto na viagem: "))
velocidade = float(input("Digite a velocidade média da viagem: "))

distancia = tempo * velocidade

litros_usados = distancia / 12

print(f"\nVelocidade média:  {velocidade} km/h")
print(f"Tempo gasto na viagem: {tempo}")
print(f"Distancia percorrida: {distancia}")
print(f"Quantidade de litros utilizada na Viagem: {litros_usados:.1f}")
