#=====================================================Código em Python======================================================================================================================================================================
# Objetivo da tarefa

# Utilize o comando 'input' para receber ao menos 2 números de entrada do usuário;

# Converta os valores recebidos pelo usuário para número inteiro (int) ou ponto flutuante (float);

# Implemente ao menos 4 operações matemáticas em seu código;

# Adicione um laço de repetição ou uma condicional. Por exemplo: você pode permitir que o usuário escolha qual operação realizar ou criar um loop que permita ao usuário realizar várias operações consecutivas;

# Utilize o comando 'print' para exibir o resultado da operação matemática.

#===========================================================================================================================================================================================================================================

# Definindo as funções
def Dicionario():
  alunos_notas = {} #Cria o Dicionário
  contador = int(input("\nQuantas notas serão registradas: "))
  for i in range(contador): #Preenche o dicionário
    nome_aluno = input(f"\nDigite o nome do aluno {i+1}: ")
    nota_aluno = float(input(f"\nDigite a nota de {nome_aluno}: "))
    alunos_notas[nome_aluno] = nota_aluno
  return alunos_notas, contador # Retorna o dicionário e conta


def Media(alunos_notas, contador):
  soma = 0
  for nota in alunos_notas.values():
    soma += nota #Soma as notas dentro do dicionário
  media_notas = soma/contador #Faz a média geral da soma das notas
  print(f"\nA média da turma é: {media_notas:.2f}")
  return media_notas # Retorna a média

def Variancia(alunos_notas, media_notas):
  soma_quadrados_diferencas = sum([(nota - media_notas)**2 for nota in alunos_notas.values()])
  variancia = soma_quadrados_diferencas / len(alunos_notas)
  print(f"\nA variância das notas é: {variancia:.2f}")
  return variancia # Retorna a variancia

def Desvio_padrao(variancia):
  desvio_padrao = variancia**0.5
  print(f"\nO desvio padrão das notas é: {desvio_padrao:.2f}")
# Não retorna nada

def Media_Nota(alunos_notas):
  med_ano = 6
  for nome_aluno, nota in alunos_notas.items(): #Pega a nota de cada aluno e subtrai pela média da escola
    if nota >= med_ano: #Averigua se o aluno passou de ano ou não
      print(f"\n{nome_aluno}: Aprovado") #Printa o nome do aluno e se foi aprovado ou não
    else:
      print(f"\n{nome_aluno}: Reprovado")


# Escolhendo o tipo de calculo que se deseja fazer
alunos_notas = {}
contador = 0
while True:
  print("\n escolha a opção desejada:")
  print("1. Criar a lista com o nome e a nota dos alunos")
  print("2. Média da turma")
  print("3. Variância")
  print("4. Desvio Padrão")
  print("5. Verificar aprovação de ano")
  print("6. Sair")

  escolha = int(input("\nDigite o número da sua escolha:"))

  if escolha == 1:
    alunos_notas, contador = Dicionario()
  elif escolha == 2:
    if alunos_notas: # Checagem para ver se o dado existe
      media_notas = Media(alunos_notas, contador)
    else:
      print("\nPor favor, crie a lista de alunos e notas primeiro (Opção 1).")
  elif escolha == 3:
    if alunos_notas: # Checagem para ver se o dado existe
      # Calculo da média
      media_notas = Media(alunos_notas, contador)
      Variancia(alunos_notas, media_notas)
    else:
      print("\nPor favor, crie a lista de alunos e notas primeiro (Opção 1).")
  elif escolha == 4:
    if alunos_notas: # Checagem para ver se o dado existe
      # Calculando a variancia primeiro
      media_notas = Media(alunos_notas, contador)
      variancia = Variancia(alunos_notas, media_notas)
      Desvio_padrao(variancia)
    else:
      print("\nPor favor, crie a lista de alunos e notas primeiro (Opção 1).")
  elif escolha == 5:
    if alunos_notas: # Checagem para ver se o dado existe
      Media_Nota(alunos_notas)
    else:
      print("\nPor favor, crie a lista de alunos e notas primeiro (Opção 1).")
  elif escolha == 6: # Sai do programa
    print("\nSaindo do programa...")
    break
  else:
    print("\nOpção invalida!")


    
