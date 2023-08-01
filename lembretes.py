from datetime import datetime

def adicionar_lembrete(lembretes, nome, data):
    try:
        data_lembrete = datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print("Formato de data inválido. Use o formato YYYY-MM-DD. ")
        return
    
    data_lembrete = data_lembrete.date()
    data_atual = datetime.now()
    data_atual = data_atual.date()

    if data_lembrete < data_atual:
        print('\nData inválida. Insira uma data no futuro.\n')
        return
    
    if data_lembrete in lembretes:
        lembretes[data_lembrete].append(nome)
        print('Lembrete adicionado com sucesso!')
    else:          
        lembretes[data_lembrete] = [nome]
        print('Lembrete adicionado com sucesso!')
    
    lembretes = ordenar_lembretes(lembretes)
    imprimir_lembretes(lembretes)

def ordenar_lembretes(lembretes):
    lembretes_ordenados = {data: lembretes[data] for data in sorted(lembretes.keys())}
    return lembretes_ordenados

def excluir_lembretes(lembretes):
    print('Para excluir um lembrete digite a data e o índice do lembrete que deve ser excluido.')
    data = input('Digite a data: ')
    data_lembrete = datetime.strptime(data, "%Y-%m-%d")
    data_lembrete = data_lembrete.date()
    index = int(input('Digite o índice: '))
    del lembretes[data_lembrete][index]

def imprimir_lembretes(lembretes):
    print('\n ===== LISTA DE LEMBRETES ===== \n')
    
    for data, nome in lembretes.items():
        if nome is None:
            break
        print(f"\n{data}\n")
        for index, nome in enumerate(nome):
            print(f"\t [{index}] - {nome}") 
    print('\n\n')

def main():
     
    lembretes = {} 

    while True:   

        print('===== MENU =====')
        print('Opções disponíveis: ')
        print('1 - Adicionar lembrete')
        print('2 - Mostrar lembretes salvos')
        print('3 - Deletar lembrete')
        print('0 - Sair')     

        opcao = input('\nDigite a opção desejada: ')

        if opcao == '1':            
            nome = input('Insira o nome do lembrete: ')
            while nome == '':
                print('O nome não foi preenchido.')
                nome = input('Insira o nome do lembrete: ')

            data = input('Insira a data do lembrete (no formato YYYY-MM-DD): ')
            while data == '':
                print('A data não foi preenchida.')        
                data = input('Insira a data do lembrete no formato YYYY-MM-DD: ')
            adicionar_lembrete(lembretes, nome, data)            

        elif opcao == '2':            
            imprimir_lembretes(lembretes)

        elif opcao == '3':            
            excluir_lembretes(lembretes)

        elif opcao == '0':
            print('Saindo do programa...')
            break
        
        else:
            print('\n Opção inválida. Digite novamente\n')

main()
