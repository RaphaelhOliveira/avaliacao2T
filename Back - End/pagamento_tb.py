print(" SISTEMA DE PAGAMENTOS ")

valor_valido = False
while not valor_valido:
    try:
        valor = float(input("\nDigite o valor do pagamento: R$ "))
        if valor > 0:
            valor_valido = True
        else:
            print("Valor deve ser maior que zero!")
    except:
        print("Digite apenas números (ex: 50.99)")

print("\nFORMAS DE PAGAMENTO:")
print("1 - Cartão de Crédito")
print("2 - PIX")
print("3 - Boleto")

opcao = input("Escolha (1/2/3): ")

if opcao == "1":
    forma = "CARTÃO DE CRÉDITO"
    status = "PAGO" 
elif opcao == "2":
    forma = "PIX"
    status = "PAGO"
elif opcao == "3":
    forma = "BOLETO"
    status = "PENDENTE"  
else:
    forma = "INVÁLIDA"
    status = "NÃO PROCESSADO"

print("\n📄 COMPROVANTE:")
print(f"Valor: R$ {valor:.2f}")
print(f"Forma: {forma}")
print(f"Status: {status}")

if status == "PAGO":
    print("\n✅ Pagamento aprovado!")
else:
    print("\n⚠️ Aguardando pagamento...")

print("\nObrigado por usar nosso sistema!")
