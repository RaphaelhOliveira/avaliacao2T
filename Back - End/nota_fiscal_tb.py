print("==Gerador de Nota Fiscal==")

chave_acesso = input("Digite a chave de acesso (10 dígitos): ")
while len(chave_acesso) != 10 or not chave_acesso.isdigit():
    print("Chave inválida! Deve ter 10 dígitos numéricos.")
    chave_acesso = input("Digite novamente: ")

data_emissao = input("Digite a data de emissão (DD/MM/AAAA): ")

itens = []
print("\nAdicione os itens (digite 'fim' para terminar):")
while True:
    item = input("\nNome do item: ")
    if item.lower() == 'fim':
        break
    quantidade = int(input("Quantidade: "))
    valor_unitario = float(input("Valor unitário (R$): "))
    itens.append({
        'item': item,
        'quantidade': quantidade,
        'valor_unitario': valor_unitario,
        'total': quantidade * valor_unitario
    })


valor_total = sum(item['total'] for item in itens)

print("\n" + "=" * 50)
print("NOTA FISCAL".center(50))
print("=" * 50)
print(f"Chave: {chave_acesso}")
print(f"Data: {data_emissao}")
print("\nITENS:")
for i, item in enumerate(itens, 1):
    print(f"{i}. {item['item']} - {item['quantidade']} x R$ {item['valor_unitario']:.2f} = R$ {item['total']:.2f}")
print("\n" + "-" * 50)
print(f"VALOR TOTAL: R$ {valor_total:.2f}".rjust(50))
print("=" * 50)
print("NOTA GERADA COM SUCESSO!")
