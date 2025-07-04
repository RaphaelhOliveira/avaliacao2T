def cadastrar_usuario():
    print("=== CADASTRO DE USUÁRIO ===")
    
    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    endereco = input("Endereço: ")
    cpf = input("CPF (apenas números): ")
    
    while len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido! Deve conter 11 dígitos numéricos.")
        cpf = input("CPF (apenas números): ")
    
    print("\n=== DADOS CADASTRADOS ===")
    print(f"Nome: {nome}")
    print(f"Telefone: {telefone}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
    
    salvar = input("\nDeseja salvar este cadastro? (S/N): ").upper()
    if salvar == 'S':
        print("Cadastro salvo com sucesso!")
    else:
        print("Cadastro descartado.")

cadastrar_usuario()
