#Uma forma de criar um arquivo em excel, através do python
#Se rodar o código, o arquivo será criado

import xlsxwriter
import os

#Onde o arquivo será criado
nomeCaminhoArquivo = 'C:\\Users\\viola\\OneDrive\\Documentos\\CURSOS TECNOLOGIA\\UDEMY\\pythonProject\\PYTHON_COM_EXCEL\\meu primeiro arquivo Excel Python.xlsx'

workbook = xlsxwriter.Workbook(nomeCaminhoArquivo)

worksheet = workbook.add_worksheet() #Cria uma nova planilha em branco com o nome  sheet1

#Adcionando dados na worksheet
worksheet.write("A1", "Nome")
worksheet.write("B1", "Idade")
worksheet.write("A2", "Reginaldo")
worksheet.write("B2", "27")

#Fechando o arquivo
workbook.close()

#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)