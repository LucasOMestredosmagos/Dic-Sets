alunos = {}

while True:
    print("Opções")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Informe o nome do aluno: ")
        matricula = input("Informe a matrícula do aluno: ")
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso")
        
    elif opcao == "2":
        matricula = input("Informe a mtrícula do aluno a ser removido: ")
        if matricula in alunos:
            del alunos[matricula]
            print("Aluno removido com sucesso!")
        else:
            print("Aluno não encontrado!")
    
    elif opcao == "3":
        if alunos:
            print("Alunos registrados")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula}, Nome: {nome}")
        else:
            print("Nenhum aluno resgistrado!")
    
    elif opcao == "4":
        print("Até breve!") 
        break
    
    else:
        print("Opção inválida. Tente novamente!")               
                            
    
                