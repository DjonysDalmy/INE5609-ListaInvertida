# Trabalho Final - INE5609 - Estrutura de Dados

- ## Lista invertida

### Desenvolvedores

- Djonys Dalmy de Oliveira
- Guilherme Pinheiro

### Como usar

Execute

```bash
python3 main.py
```

Você será questionado se quer usar um conjunto de dados pré-estabelecido, se sim digite "s".

O programa irá exibir o conjunto no qual será realizado as buscas **(Opções 1, 2 e 3)**
Após cada busca o conjunto será atualizado para o resultado dessa última busca, ou seja, a próxima busca realizada quando o menu atualizar será combinada com a busca anterior e assim sucessivamente.

Caso queira fazer uma busca simples após já ter executado uma busca no programa anteriormente utilize a **(Opção 4)** para limpar o conjunto selecionado e ter toda a base de dados à disposição.

Caso caia em uma busca que não possua resultado o conjunto será resetado.

Ao incluir uma nova pessoa **(Opção 5)** o conjunto será resetado.

Ao remover uma pessoa **(Opção 6)** esta também será removida do conjunto selecionado.

A **(Opção 7)** exibir todas as pessoas da lista de dados e a **(Opção 8)** exibe apenas aquelas que estão no conjunto selecionado.

Utilize a **(Opção 9)** para finalizar o programa.

### Descrição

Utilizamos o conceito de Lista Invertida para uma busca mais rápida eficiente dos dados do banco. Ao invés de fazermos uma busca tradicional (Percorrendo item por item) mantemos salvo uma lista secundária para cada coluna de dados com  ahierarquia de informação invertida. Exemplo:

**Lista original:**
*id: Nome,Cidade,Estilo Musical,Salário*
- 1: Pedro,Florianópolis,Rock,2000.0
- 2: João,Palhoça,Funk,2000.0
- 3: Carlos,São José,Rock,4000.0
- 4: Cleiton,São José,Sertanejo,1500.0
- 5: Kebler,São José,Funk,1700.0

**Lista invertida (Cidade):**
- Florianópolis: {1}
- Palhoça: {2}
- São José: {3,4,5}

**Lista invertida (Estilo Musical):**
- Rock: {1,3}
- Funk: {2,5}
- Sertanejo: {4}

**Lista invertida (Salário):**
- 1500.0: {4}
- 1700.0: {5}
- 2000.0: {1,2}
- 4000.0: {3}

Decidimos dividir o programa entre a classe *Lista_Invertida* (Que contém as operações principais para interação com a nossa lista de dados), *Elemento* (Tudo relativo aos elementos que estão dentro dessa lista principal), *DiretorioDiscreto* e *DiretorioContinuo* (Estes dois como forma subdividir classes diferente de diretórios que compõem a lista principal, uma vez que possuem regras diferentes de inserção/comportamento/etc)
