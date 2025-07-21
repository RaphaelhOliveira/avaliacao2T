codigo = "xandao10"
desconto = 10  
valido_ate = "31/12/2025"

print("=== CUPOM DE DESCONTO ===")
print("Código:", codigo)
print("Desconto:", desconto, "%")
print("Válido até:", valido_ate)

usar = input("Digite o código do cupom: ")

if usar == codigo:
    print("Cupom aplicado! Você ganhou", desconto, "% de desconto.")
else:
    print("Cupom inválido.")
