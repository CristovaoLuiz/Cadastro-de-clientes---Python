clientes = []

while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Cliente")
    print("2 - Alterar Cliente")
    print("3 - Excluir Cliente")
    print("4 - Listar Clientes")
    print("5 - Sair")

    opcao = input("Digite sua opção: ")

    if opcao == '1':
        nome = input("Digite o nome do cliente: ")
        clientes.append(nome)
        print(f"Cliente {nome} cadastrado com sucesso! ")
        
    elif opcao == '2':
        if not clientes:
            print("Ops! Não tem clientes cadastrados ainda. ")
            continue
        print("\nClientes Cadastrados:")
        for i, nome in enumerate(clientes):
            print(f"{i+1} - {nome}")
        index = int(input("Digite o número do cliente a ser alterado: ")) - 1
        if 0 <= index < len(clientes):
            novo_nome = input("Digite o novo nome: ")
            clientes[index] = novo_nome
            print(f"Cliente alterado com sucesso! ")
        else:\
            print("Índice inválido! ")
    elif opcao == '3':
        if not clientes:
            print("Ops! Não tem clientes para excluir. ")
            continue
        print("\nClientes Cadastrados:")
        for i, nome in enumerate(clientes):
            print(f"{i+1} - {nome}")
        index = int(input("Digite o número do cliente a ser excluído: ")) - 1
        if 0 <= index < len(clientes):
            nome_excluido = clientes.pop(index)
            print(f"Cliente {nome_excluido} excluído com sucesso! ")
        else:
            print("Índice inválido! ")
    elif opcao == '4':
        if not clientes:
            print("Ainda não tem clientes cadastrados, miga! 🤷")
        else:
            print("\nClientes Cadastrados:")
            for nome in clientes:
                print(f'- {nome}')
    elif opcao == '5':
        print("Tchau, tchau! ")
        break
    else:
        print("Opção inválida! Tente de novo. ")
