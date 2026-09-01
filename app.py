# Programa de cálculo de consumo elétrico e valor mensal médio gasto 
# # Autor: Cristian
# Entrada 
nome = input("Digite o nome do aparelho elétrico: ") 
potencia = float(input("Digite a sua potência em watts: ")) 
horasDia = float(input("Digite o tempo médio de uso diário em horas: ")) 
# Processamento
if potencia <= 0 or horasDia <= 0:
    print("Valores inválidos. Por favor, digite valores positivos.")
else:
    custoKW = 0.75
    consumoMensal = (potencia * horasDia * 30)/1000
    valorMensal = consumoMensal * custoKW
    # Saída 
    print(f"\nAparelho: {nome}") 
    print(f"Consumo estimado: {consumoMensal:.2f}Kw") 
    print(f"Valor mensal médio gasto: R${valorMensal:.2f}")
