# Programa de cálculo de consumo elétrico e valor mensal médio gasto 
# Autor: Cristian
# Entrada 
nome = input("Digite o nome do aparelho elétrico: ") # captura nome digitado e guarda na variavel nome
potencia = float(input("Digite a sua potência em watts: ")) # captura caracter digitado, transforma em numero do tipo float e guarda na variavel potencia
horasDia = float(input("Digite o tempo médio de uso diário em horas: ")) # captura caracter digitado, transforma em numero do tipo float e guarda na variavel horasDia
# Processamento
if potencia <= 0 or horasDia <= 0: # compara valores das variaveis potencia e horasDia se é menor ou igual a zero, se for entra na linha abaixo
    print("Valores inválidos. Por favor, digite valores positivos.") # se variveis acima iguais ou menores que zero imprime esse texto na tela
else: # se valores maiores que zero entra na linha abaixo 
    custoKW = 0.75 # R$0.75 é o custo do Kw
    consumoMensal = (potencia * horasDia * 30)/1000 # formula do consumo mensal
    valorMensal = consumoMensal * custoKW # formula do valor mensal
    # Saída 
    print(f"\nAparelho: {nome}") # imprime na tela o nome do aparelho
    print(f"Consumo estimado: {consumoMensal:.2f}Kw") # imprime na tela o consumo mensal com dois digitos após a virgula
    print(f"Valor mensal médio gasto: R${valorMensal:.2f}") # imprime na tela o valor mensal com dois digitos após a virgula
