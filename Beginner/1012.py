# Todas as Entradas na Mesma Linha Graças ao Método Split
A, B, C = input().split()

# Conversão Dos Valores de Entrada Para Tipo Float
A = float(A)
B = float(B)
C = float(C)

# Variáveis Com Seus Respectivos Cálculos
Triangulo = (A * C) / 2
Circulo = 3.14159 * (C ** 2)
Trapezio = ((A + B) * C) / 2
Quadrado = B * B
Retangulo = A * B

# Exibições em Ordem
print(f"TRIANGULO: {Triangulo:.3f}")
print(f"CIRCULO: {Circulo:.3f}")
print(f"TRAPEZIO: {Trapezio:.3f}")
print(f"QUADRADO: {Quadrado:.3f}")
print(f"RETANGULO: {Retangulo:.3f}")