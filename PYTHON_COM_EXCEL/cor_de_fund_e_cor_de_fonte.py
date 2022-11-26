#Uma forma de criar um arquivo em excel, através do python
#Se rodar o código, o arquivo no excel será criado

import xlsxwriter
import os
import datetime

#Onde o arquivo será criado
nomeCaminhoArquivo = 'C:\\Users\\viola\\OneDrive\\Documentos\\CURSOS TECNOLOGIA\\UDEMY\\pythonProject\\PYTHON_COM_EXCEL\\meu terceiro arquivo Excel Python.xlsx'

workbook = xlsxwriter.Workbook(nomeCaminhoArquivo)

workbook.set_properties({
    'category': "Estudante",
    'title': "Meu segundo arquivo de excel usando o Python",
    'Subject': "Aula Python Excel",
    'Author': "Curso online",
    'company': "Reginaldo Alves",
    'keywords': "Estudante",
    'create': datetime.date(2022,11,23),
    'comments': "Bons estudos"
})

worksheet = workbook.add_worksheet("Dados") #Cria uma nova sheet em branco com o nome Dados

#Armazena a cor amarela para ser usada como cor de fundo da céular
cor_fundo = workbook.add_format()
cor_fundo.set_fg_color("yellow")

#Armazena a cor azul para ser usada como cor de fonte na célula
cor_fonte = workbook.add_format()
cor_fonte.set_font_color('blue')

worksheet.write("A1", "Nome",cor_fundo)
worksheet.write("B1", "Idade",cor_fundo)
worksheet.write("A2", "Reginaldo")
worksheet.write("B2", 27,cor_fonte)

worksheet.write("A3", "Renato")
worksheet.write("B3", 51,cor_fonte)

worksheet.write("A4", "Aneilde")
worksheet.write("B4", 50,cor_fonte)



#Fechando o arquivo
workbook.close()

#Abrindo o arquivo
os.startfile(nomeCaminhoArquivo)
