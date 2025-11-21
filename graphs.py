# ====================================================================================================================================================

# Faça uma análise detalhada dos dados, descubra quais dados gostaria de destacar e crie os seguintes gráficos:

# Gráfico de Histograma

# Gráfico de dispersão

# Mapa de calor

# Gráfico de barra

# Gráfico de pizza

# Gráfico de densidade

# Gráfico de Regressão

# Adicione títulos nos gráficos e nos eixos para ficar claro os objetivos dos gráficos

# ====================================================================================================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento dos dados ============================================================================================================================
df=pd.read_csv('ecommerce_preparados.csv')
# print(df.head())

# Análise inicial dos dados ==========================================================================================================================

# print(df.info())
# print(df['Marca'].describe())
# print(df['Qtd_Vendidos'])
# print(df['Marca'].isnull().sum())
# print(df['Preço'].isnull().sum())

# Tratemento dados ==================================================================================================================================

# Qtd_Vendidos
df['Quantidade Vendida'] = df['Qtd_Vendidos'].apply(lambda x:float(x.replace('+', '').replace('mil', '000').replace('Nenhum', '0')))
# print(df['Quantidade Vendida'])
# print(df.info())


# Marca
df = df[df['Marca'] != 'não definido']
df['Marca'] = df['Marca'].str.title()


# Gênero
Dic_ge={
    'Mulher':'Feminino',
    'roupa para gordinha pluss P ao 52': 'Feminino', 
    'bermuda feminina brilho Blogueira': 'Feminino',
    'Sem gênero': 'Unissex',
    'bebê': 'Bebês',
    'Sem gênero infantil': 'Unissex Infantil',
    'masculino': 'Masculino',
    'menino': 'Meninos',
    'short menina verao look mulher': 'Meninas'}

# Substituição dos valores e contagem
df['Gênero_V'] = df['Gênero'].replace(Dic_ge, regex=False)
# print(df['Gênero_V'].value_counts())
df['Gênero_V'] = df['Gênero_V'].str.title()


# Gráficos ===========================================================================================================================================

# 1- Gráfico de Histograma
# plt.figure(figsize=(10, 6))
# sns.histplot(df['Preço'], bins=50, binrange=(0, 600), color='green', kde=True, binrange=(0, 600)) # binrange define o intervalo dos dados a serem plotados | kde=True: adiciona uma linha de densidade
# # plt.hist(df['Preço'], bins=50, color='green', alpha=0.8) # Pelo matplotlib
# plt.xticks(range(0, 601, 50)) # Define os ticks do eixo x de 0 a 600 com intervalos de 50
# plt.xticks(rotation=45) # Rotaciona os ticks do eixo x para melhor visualização
# plt.title('Distribuição das Preço')
# plt.xlabel('Preço')
# plt.ylabel('Frequência')
# plt.show()


# 2- Gráfico de dispersão
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='Desconto', y='Preço', data=df, hue='Gênero_V', palette='Set2', alpha=0.7)
# plt.scatter(df['Desconto'], df['Preço'], alpha=0.5) # Pelo matplotlib
# plt.legend(title='Gênero', loc='upper right') # bbox_to_anchor=(0.8, 1) | bbox_to_anchor posiciona a legenda fora do gráfico
# plt.title('Relação entre Desconto e Preço')
# plt.xlabel('Desconto (%)')
# plt.ylabel('Preço')
# plt.show()

# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='Nota', y='N_Avaliações', data=df, hue='Gênero_V', palette='Set2', alpha=0.7)
# # plt.scatter(df['Nota'], df['N_Avaliações'], alpha=0.5) # Pelo matplotlib
# plt.title('Relação entre Nota e Número de Avaliações por Gênero')
# plt.xlabel('Nota')
# plt.ylabel('Número de Avaliações')
# plt.show()


# # 3- Mapa de calor
# plt.figure(figsize=(12, 8))
# corr_matrix=df[['Preço_MinMax', 'Desconto_MinMax', 'Nota_MinMax', 'Qtd_Vendidos_Cod']].corr()
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Mapa de Calor das Correlações entre Preço, Desconto, Nota e Quantidade Vendida')
# plt.show()


# # 4- Gráfico de barra
# plt.figure(figsize=(12, 6))
# top_marcas = df['Marca'].value_counts().head(10)
# # sns.barplot(x=top_marcas.index, y=top_marcas.values, palette='viridis')
# plt.bar(top_marcas.index, top_marcas.values, color=sns.color_palette('viridis', n_colors=10)) # Pelo matplotlib
# plt.xticks(rotation=45)
# plt.title('Top 10 Marcas com Mais Produtos')
# plt.xlabel('Marca')
# plt.ylabel('Número de Produtos')
# plt.show()


# # 5- Gráfico de pizza
# plt.figure(figsize=(10, 8))
# plt.pie(df['Gênero_V'].value_counts(), labels=df['Gênero_V'].value_counts().index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel')) # autopct adiciona a porcentagem em cada fatia
# plt.title('Distribuição de Produtos por Gênero')
# plt.legend(df['Gênero_V'].value_counts().index, title='Gênero', loc='best', bbox_to_anchor=(0.1, 1.05)) # bbox_to_anchor posiciona a legenda fora do gráfico
# plt.show()


# # 6- Gráfico de densidade
# plt.figure(figsize=(10, 6))
# sns.kdeplot(df['Nota'], shade=True, color='blue')
# plt.title('Distribuição de Densidade das Notas dos Produtos')
# plt.xlabel('Nota')
# plt.ylabel('Densidade')
# plt.show()


# # 7- Gráfico de Regressão
# plt.figure(figsize=(10, 6))
# sns.regplot(x='Nota_MinMax', y='N_Avaliações_MinMax', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
# plt.title('Relação entre Nota e Número de Avaliações')
# plt.xlabel('Nota (MinMax)')
# plt.ylabel('Número de Avaliações (MinMax)')
# plt.show()

