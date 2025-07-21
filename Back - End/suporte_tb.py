mensagem = input("Digite sua mensagem de suporte: ")
data = input("Digite a data (ex: 21/07/2025): ")
status = "Aberto"

print("\n=== CHAMADO DE SUPORTE ===")
print("Mensagem:", mensagem)
print("Data:", data)
print("Status:", status)

resposta = input("\nDeseja marcar o chamado como resolvido? (s/n): ")

if resposta == "s":
    status = "Resolvido"
    print("Status atualizado para:", status)
else:
    print("O chamado continua com status:", status)
