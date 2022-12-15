from elemento import Elemento
from diretorio_continuo import DiretorioContinuo
from diretorio_discreto import DiretorioDiscreto
from time import sleep

class Lista_Invertida:
  def __init__(self):
    self.lista_elementos = []
    self.cidades = DiretorioDiscreto
    self.times = DiretorioDiscreto
    self.estilos_musicais = DiretorioContinuo

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
    print(('1 - Buscar por cidade\n2 - Buscar por estilo musical\n3 - Buscar por salário\n4 - Fazer busca composta\n5 - Incluir nova pessoa\n6 - Remover pessoa\n7 - Exibir todas as pessoas'))
    resposta = int(input('\nEscolha sua opção: '))
    if resposta in [1, 2, 3, 4, 5, 6, 7]:
      return resposta
    else:
      print('\nResposta não encontrada!')
      self.menu()

  def buscar_por_criterio(self, index):
    pass

  def verifica_lista_vazia(self):
    if len(self.lista_elementos) == 0:
      print('\nNão temos nenhum elemento na lista')
      return True
    else:
      return False
      
  def iniciar_programa(self):
    pergunta = input('Você deseja carregar a carga de dados? ')
    if self.verifica_resposta(pergunta):
      self.carregar_cargo_de_dados()
      print('Aqui está a lista de elementos:')
      for elemento in self.lista_elementos:
        print(f'ID: {elemento.id} - Nome: {elemento.nome}, Cidade: {elemento.cidade}, Estilo Musical: {elemento.estilo_musical}, Salário: {elemento.salario}')
    else:
      print('\nOk! Vamos iniciar sem dados...')
    resposta_menu = self.menu()
    if resposta_menu == 1:
      if self.verifica_lista_vazia() is False:
        pass
      else:
        print('teste')
    elif resposta_menu == 2:
      if self.verifica_lista_vazia() is False:
        pass
    elif resposta_menu == 3:
      if self.verifica_lista_vazia() is False:
        pass
    elif resposta_menu == 4:
      if self.verifica_lista_vazia() is False:
        pass
    elif resposta_menu == 5:
      if self.verifica_lista_vazia() is False:
        pass
    elif resposta_menu == 6:
      if self.verifica_lista_vazia() is False:
        pass
    elif resposta_menu == 7:
      if self.verifica_lista_vazia() is False:
        pass
