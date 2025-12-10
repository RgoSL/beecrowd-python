# Variáveis Que Recebem os Valores do Cálculo
Peca1_codigo, Peca1_qtd, Peca1_preco = input().split() # Uso do Método Split Para 1 Input Servir Para 3 Variáveis na Mesma Linha
Peca2_codigo, Peca2_qtd, Peca2_preco = input().split()

# Conversão Dos Valores Das Variáveis de Código Para Int
Peca1_codigo = int(Peca1_codigo)
Peca2_codigo = int(Peca2_codigo)

# Conversão Dos Valores Das Variáveis de Quantidade Para Int
Peca1_qtd = int(Peca1_qtd)
Peca2_qtd = int(Peca2_qtd)

# Conversão Dos Valores Das Variáveis de Preço Para Float
Peca1_preco = float(Peca1_preco)
Peca2_preco = float(Peca2_preco)

ValorPago = (Peca1_qtd * Peca1_preco) + (Peca2_qtd * Peca2_preco)

print(f"VALOR A PAGAR: R$ {ValorPago:.2f}")