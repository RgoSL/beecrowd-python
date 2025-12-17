# Entrada de Inteiros
A, B, C, D = input().split() # Método Split Para Encaixar Todas as Variáveis no Mesmo Input

# Conversão de Cada Variável Para o Tipo Inteiro
A = int(A)
B = int(B)
C = int(C)
D = int(D)

# Uso do Operador Lógico AND Para Exibir True em Caso de Múltiplas Validações
if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and (A % 2 == 0): # Estrutura de Condição do Problema
    print("Valores aceitos")   
else:
    print("Valores nao aceitos")