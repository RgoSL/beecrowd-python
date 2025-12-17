# Entrada Dos Pontos Cartesianos
X1, Y1 = input().split() # Uso do Método Split Para Receber Mais de um Dado no Mesmo Input
X2, Y2 = input().split() 

# Conversão Dos Pontos X Para o Tipo de Dados Real
X1 = float(X1)
X2 = float(X2)

# Conversão Dos Pontos Y Para o Tipo de Dados Real
Y1 = float(Y1)
Y2 = float(Y2)

# Uso de " ** 0.5 " Para Representar Uma Raíz Quadrada Sem Usar Libs Externas ou Métodos Prontos
Distancia = ((X2 - X1) ** 2 + (Y2 - Y1) ** 2) ** 0.5 # Variável Que Armazena o Cálculo da Distância Entre os Pontos

# Exibição da Distância Formatada Com 4 Casas Decimais
print(f"{Distancia:.4f}")