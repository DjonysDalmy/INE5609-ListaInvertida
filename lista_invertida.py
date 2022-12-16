from elemento import Elemento
from diretorio_continuo import DiretorioContinuo
from diretorio_discreto import DiretorioDiscreto
from time import sleep

class Lista_Invertida:
  def __init__(self):
    self.lista_elementos = []
    self.cidades = DiretorioDiscreto()
    self.estilos_musicais = DiretorioDiscreto()
    self.salarios = DiretorioContinuo()

  def verifica_resposta(self, pergunta):
    if pergunta.upper() == 'S':
      return True
    elif pergunta.upper() == 'N':
      return False

  def carregar_cargo_de_dados(self):
    carga_de_dados = [Elemento(1, "Pedro", "Florianópolis", "Rock", 1500.5), Elemento(2, "João", "Florianópolis", "Funk", 5500.5), Elemento(3, "Rafaela", "São José", "MPB", 2500.83), Elemento(4, "Júlia", "Palhoça", "Sertanejo", 7200.0), Elemento(5, "Germán", "Buenos Aires", "Tango", 2100.55), Elemento(6, "Juan", "Florianópolis", "Rock", 3400.2), Elemento(7, "Joana", "Palhoça", "Funk", 4500.4), Elemento(8, "Letícia", "Florianópolis", "Pagode", 2000.7), Elemento(9, "Thiago", "São José", "Rock", 9800.0), Elemento(10, "Marcelo", "Palhoça", "MPB", 7050.7)]
    for elemento in carga_de_dados:
      self.lista_elementos.append(elemento) 

  def menu(self):
    sleep(3)
    print('\nEscolha uma das opções:')
    print(('1 - Buscar por cidade\n2 - Buscar por estilo musical\n3 - Buscar por salário\n4 - Fazer busca composta\n5 - Incluir nova pessoa\n6 - Remover pessoa\n7 - Exibir todas as pessoas\n8 - Sair'))
    resposta = int(input('\nEscolha sua opção: '))
    if resposta in [1, 2, 3, 4, 5, 6, 7, 8]:
      return resposta
    else:
      print('\nResposta não encontrada!')
      self.menu()

  def menu_busca_composta(self):
    pass

  def carregar_diretorios(self):
    for elemento in self.lista_elementos:
      self.cidades.acrescentar_item_diretorio(elemento.cidade, elemento.id)
      self.estilos_musicais.acrescentar_item_diretorio(elemento.estilo_musical, elemento.id)
      self.salarios.acrescentar_item_diretorio(elemento.salario, elemento.id)

  def verifica_lista_vazia(self):
    if len(self.lista_elementos) == 0:
      print('\nNão temos nenhum elemento na lista')
      return True
    else:
      return False
      
  def adicionar_pessoa(self):
    id = len(self.lista_elementos) + 1
    nome = input('Informe o nome da nova pessoa: ')
    cidade = input('Informe a cidade da nova pessoa: ')
    estilo_musical = input('Informe o estilo musical da nova pessoa: ')
    salario = input('Informe o salário da nova pessoa: ')
    nova_pessoa = Elemento(id, nome, cidade, estilo_musical, salario)
    self.lista_elementos.append(nova_pessoa)
    self.cidades.acrescentar_item_diretorio(nova_pessoa.cidade, nova_pessoa.id)
    self.estilos_musicais.acrescentar_item_diretorio(nova_pessoa.estilo_musical, nova_pessoa.id)
    self.salarios.acrescentar_item_diretorio(nova_pessoa.salario, nova_pessoa.id)
    print('Pessoa adicionada com sucesso!')

  def remover_pessoa(self):
    id_pessoa_excluida = int(input('Informe o ID da pessoa que quer excluir: '))

    for pessoa in self.lista_elementos:
      if id_pessoa_excluida == pessoa.id:
        cidade_pessoa_excluida = pessoa.cidade
        estilo_musical_pessoa_excluida = pessoa.estilo_musical
        salario_pessoa_excluida = pessoa.salario

        for cidade in self.cidades.dados_diretorio:
          if cidade[0] == cidade_pessoa_excluida:
            cidade[1].remove(id_pessoa_excluida)
            if len(cidade[1]) == 0:
              self.cidades.dados_diretorio.remove(cidade)
              for i in range (0, len(self.cidades.chaves_cadastradas)):
                if cidade_pessoa_excluida == self.cidades.chaves_cadastradas[i]:
                  self.cidades.chaves_cadastradas.remove(cidade_pessoa_excluida)

        for estilo_musical in self.estilos_musicais.dados_diretorio:
          if estilo_musical[0] == estilo_musical_pessoa_excluida:
            estilo_musical[1].remove(id_pessoa_excluida)
            if len(estilo_musical[1]) == 0:
              self.estilos_musicais.dados_diretorio.remove(estilo_musical)
              for i in range (0, len(self.estilos_musicais.chaves_cadastradas)):
                if estilo_musical_pessoa_excluida == self.estilos_musicais.chaves_cadastradas[i]:
                  self.estilos_musicais.chaves_cadastradas.remove(estilo_musical_pessoa_excluida)
            
        for salario in self.salarios.dados_diretorio:
          if salario[0] == salario_pessoa_excluida:
            salario[1].remove(id_pessoa_excluida)
            if len(salario[1]) == 0:
              self.salarios.dados_diretorio.remove(salario)
              for i in range (0, len(self.salarios.chaves_cadastradas)):
                if salario_pessoa_excluida == self.salarios.chaves_cadastradas[i]:
                  self.salarios.chaves_cadastradas.remove(salario_pessoa_excluida)

        self.lista_elementos.remove(pessoa)
        print('Pessoa removida com sucesso!')

  def iniciar_programa(self):
    pergunta = input('Você deseja carregar a carga de dados? ')
    if self.verifica_resposta(pergunta):
      self.carregar_cargo_de_dados()
      self.carregar_diretorios()
    else:
      print('\nOk! Vamos iniciar sem dados...')
    resposta_menu = ''
    while resposta_menu != 8:
      resposta_menu = self.menu()
      if resposta_menu == 1:
        if self.verifica_lista_vazia() is False:
          for i in range(0 , len(self.cidades.chaves_cadastradas)):
            print(f'{i+1} - {self.cidades.chaves_cadastradas[i]}')
          cidade_escolhida = self.cidades.chaves_cadastradas[int(input('\nEscolha sua opção: '))-1]
          print(f'\nAs pessoas de {cidade_escolhida} são: ')
          sleep(1)
          for cidade in self.cidades.dados_diretorio:
            if cidade_escolhida == cidade[0]:
              for id in cidade[1]:
                for pessoa in self.lista_elementos:
                  if id == pessoa.id:
                    print(pessoa.nome)
        else:
          print('teste')
      elif resposta_menu == 2:
        if self.verifica_lista_vazia() is False:
          for i in range(0 , len(self.estilos_musicais.chaves_cadastradas)):
            print(f'{i+1} - {self.estilos_musicais.chaves_cadastradas[i]}')
          estilo_escolhido = self.estilos_musicais.chaves_cadastradas[int(input('\nEscolha sua opção: '))-1]
          print(f'\nAs pessoas do {estilo_escolhido} são: ')
          sleep(1)
          for estilo_musical in self.estilos_musicais.dados_diretorio:
            if estilo_escolhido == estilo_musical[0]:
              for id in estilo_musical[1]:
                for pessoa in self.lista_elementos:
                  if id == pessoa.id:
                    print(pessoa.nome)
      elif resposta_menu == 3:
        if self.verifica_lista_vazia() is False:
          for i in range(0 , len(self.salarios.chaves_cadastradas)):
            print(f'{i+1} - {self.salarios.chaves_cadastradas[i]}')
          salario_escolhido = self.salarios.chaves_cadastradas[int(input('\nEscolha sua opção: '))-1]
          print(f'\nAs pessoas de salário {salario_escolhido} são: ')
          sleep(1)
          for salario in self.salarios.dados_diretorio:
            if salario_escolhido == float(salario[0]):
              for id in salario[1]:
                for pessoa in self.lista_elementos:
                  if id == pessoa.id:
                    print(pessoa.nome)
      elif resposta_menu == 4:
        if self.verifica_lista_vazia() is False:
          pass
      elif resposta_menu == 5:
        if self.verifica_lista_vazia() is False:
          self.adicionar_pessoa()
      elif resposta_menu == 6:
        if self.verifica_lista_vazia() is False:
          self.remover_pessoa()
      elif resposta_menu == 7:
        if self.verifica_lista_vazia() is False:
          print('Aqui está a lista de elementos:')
          for elemento in self.lista_elementos:
            print(f'ID: {elemento.id} - Nome: {elemento.nome}, Cidade: {elemento.cidade}, Estilo Musical: {elemento.estilo_musical}, Salário: {elemento.salario}')
