from openpyxl import load_workbook
import os

nome_arquivo = 'C:\\Users\\viola\\OneDrive\\Documentos\\CURSOS TECNOLOGIA\\UDEMY\\pythonProject\\PYTHON_COM_EXCEL\\PythonDeletaLinhasEColunas.xlsx'
planilha_aberta = load_workbook(filename = nome_arquivo)

#Selecionando a planilha e abrindo a mesma
sheet_selecionada = planilha_aberta ['Aluno']

#Iniciando a exclusão da linha (2)
sheet_selecionada.delete_rows(2)

#Iniciando a exclusão da coluna (2)
sheet_selecionada.delete_cols(2)

#Salvando as alterações
planilha_aberta.save(filename=nome_arquivo )


#Abrindo o arquivo
os.startfile(nome_arquivo)