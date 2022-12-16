class DiretorioDiscreto:
  def __init__(self):
    self.dados_diretorio = []
    self.chaves_cadastradas = []

  def acrescentar_item_diretorio(self, dado, id):
    if dado in self.chaves_cadastradas:
      for i in range(0, len(self.dados_diretorio)):
        if dado == self.dados_diretorio[i][0]:
          self.dados_diretorio[i][1].append(id)
    else:
      self.dados_diretorio.append([f'{dado}', [id]])
      self.chaves_cadastradas.append(dado)