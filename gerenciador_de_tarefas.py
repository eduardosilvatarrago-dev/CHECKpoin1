print('GERENCIADOR DE TAREFA')
import json

lista_tarefas = []

def salvar_dados():
  with open('tarefas.json', 'w') as arquivo:
    json.dump(lista_tarefas, arquivo, indent=4)
    print('dados salvos com sucesso')

def carregar_dados():
    global lista_tarefas
    try:
      with open('tarefas.json', 'r') as arquivo:
        lista_tarefas = json.load(arquivo)
      print('dados carregados com sucesso')
    except FileNotFoundError:
      print('arquivo nao encontrado')
      lista_tarefas = []

def adicionar_tarefa(descricao):
   nova_tarefa = {'descricao': descricao,
                 'concluido': False}
   lista_tarefas.append(nova_tarefa)
   print('tarefa adicionada com sucesso')

def listar_tarefas():
  print('lista de tarefas')
  for i, tarefa in enumerate(lista_tarefas):
    status = '[x]' if tarefa['concluido'] else '[]'
    print(f'{i} - {status} {tarefa['descricao']}')
  print('______________________\n')

def concluir_tarefa(indice):
  try:
    lista_tarefas[indice]['concluido'] = True
    print('Tarefa concluida com sucesso')
  except IndexError:
    print('indice invalido')
  print('______________________\n')


carregar_dados()

while True:
    print('\n1-adicionar tarefa')
    print('2-listar tarefas')
    print('3-concluir tarefas')
    print('4-salvar e sair')
    opcao = input('Digite a opcao desejada: ')

    if opcao == '1':
        descricao = input('digite a descricao da tarefa: ')
        adicionar_tarefa(descricao)
    elif opcao == '2':
        listar_tarefas()
    elif opcao == '3':
        try:
          num = int(input('digite o numero da tarefa a ser concluida: '))
          concluir_tarefa(num)
        except ValueError:
          print('numero invalido')
    elif opcao == '4':
        salvar_dados()
        print('saindo do programa')
        break
    else:
        print('opçao invalida')
