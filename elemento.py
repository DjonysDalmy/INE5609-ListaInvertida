class Elemento:
  def __init__(self, id, nome, cidade, estilo_musical, salario):
    self.id = id
    self.nome = nome
    self.cidade = cidade
    self.estilo_musical = estilo_musical
    self.salario = salario

    @property
    def id(self):
      return self.id

    @id.setter
    def id(self, id):
      self.id = id
    
    @property
    def nome(self):
      return self.nome

    @nome.setter
    def nome(self, nome):
      self.nome = nome
    
    @property
    def cidade(self):
      return self.cidade

    @cidade.setter
    def cidade(self, cidade):
      self.cidade = cidade

    @property
    def estilo_musical(self):
      return self.estilo_musical

    @estilo_musical.setter
    def estilo_musical(self, estilo_musical):
      self.estilo_musical = estilo_musical

    @property
    def salario(self):
      return self.salario

    @salario.setter
    def salario(self, salario):
      self.salario = salario
