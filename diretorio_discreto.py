class DiretorioDiscreto:
  def __init__(self, nome, id):
    self.dados_diretorio = [nome, [id]]

  def acrescentar_item_diretorio(self, id):
    self.dados_diretorio[1].append(id)
