import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# arquivos
arquivo_excel_1 = '1e2.xlsx'
arquivo_excel_2 = '3.xlsx'

# Armazena dados
df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name = 'dia1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name = 'dia2')
df_dia_3 = pd.read_excel(arquivo_excel_2, sheet_name = 'dia3')

# Consolida dados concatena uma lista
df_consolida = pd.concat([df_dia_1,df_dia_2,df_dia_3])

# Exporta dados consolidados para uma planilha 
df_consolida.to_excel('consolida.xlsx')

# Imprimindo coluna especifica de dados consolidados
# print(df_consolida['Vendedor'])

# Agrupando dados por resultados de coluna especifica e somando
lucro_por_vendedor = df_consolida.groupby(['Vendedor']).sum()

# Imprimindo resultado agrupado e somado
# print(lucro_por_vendedor)

# relatório de todas as linhas :, da coluna Unidades até Preço
relatorio_vendedor = lucro_por_vendedor.loc[:,"Unidades" : "Preço"]

# Imprimindo relatório
print(relatorio_vendedor)

# Gerando grafico do relatorio do tipo barras
relatorio_vendedor.plot(kind='bar')

# Executando gráfico de relatorio do tipo barras
plt.show()