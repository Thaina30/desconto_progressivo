"""
Programa: Sistema de Desconto Progressivo
Descrição: Calcula o desconto e o valor final de uma compra com
           base no valor total informado pelo usuário.
Regras de desconto:
    - Valor < R$ 200,00 -> desconto de 5%
    - R$ 200,00 <= Valor < R$ 300,00 -> desconto de 10%
    - Valor >= R$ 300,00 -> desconto de 15%
"""

# Solicita ao usuário o valor total da compra
# O valor digitado é convertido para float, pois pode conter casas decimais
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Estrutura condicional para definir qual percentual de desconto será aplicado
# de acordo com a faixa em que o valor da compra se encaixa
if valor_compra < 200:
    percentual_desconto = 5
elif valor_compra < 300:
    percentual_desconto = 10
else:
    percentual_desconto = 15

# Cálculo do valor do desconto em reais
# Fórmula: valor da compra * (percentual de desconto / 100)
valor_desconto = valor_compra * (percentual_desconto / 100)

# Cálculo do valor final a ser pago (valor da compra menos o desconto)
valor_final = valor_compra - valor_desconto

# Exibição dos resultados formatados com duas casas decimais
print("\n----- Resumo da Compra -----")
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual_desconto}% (R$ {valor_desconto:.2f})")
print(f"Valor final a pagar: R$ {valor_final:.2f}")