import xlsxwriter as xls
import os
import pandas as pd

#Vamos criar um dicionário usando um DataFrame para preencher as informações na planilha.
dataFrame = pd.DataFrame({ 'Nome':   ['Reginaldo','Renato','Neide','Giovanna','Regineide'],
                           'Idade' : [27, 51, 50, 7, 28],
                           'Salário':[1000,2000,3000,4000,5000]
                        })

#Cria e salva planulha usando o pd.ExcelWriter
arquivo = pd.ExcelWriter('C:\\Users\\viola\\OneDrive\\Documentos\\CURSOS TECNOLOGIA\\UDEMY\\pythonProject\\PYTHON_COM_EXCEL\\meu quarto arquivo Excel Python.xlsx', engine = 'xlsxwriter' )

#Converte o DataFrame em um objeto Excel.
dataFrame.to_excel(arquivo, sheet_name= "Dados")

#Pega a pasta de trabalho xlsxwriter e os objetos de planilha
workbook = arquivo.book
worksheet = arquivo.sheets['Dados']

#Variavel para colocar o formato de moeda
formato_moeda = workbook.add_format({'num_format': '#,##.00'})

worksheet.set_column('D:D',None, formato_moeda)

#Fechando o arquivo
workbook.close()

#Abrindo o arquivo
os.startfile(arquivo)