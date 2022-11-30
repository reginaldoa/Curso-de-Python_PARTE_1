from openpyxl import load_workbook
import os


Caminho_arquivo = 'C:\\Users\\viola\\OneDrive\\Documentos\\CURSOS TECNOLOGIA\\UDEMY\\pythonProject\\PYTHON_COM_EXCEL\\Formulas.xlsx'
planilha_que_abrimos_com_python = load_workbook(filename = Caminho_arquivo)

#Selecionando a planilha e abrindo a mesma
sheet_selecionada = planilha_que_abrimos_com_python ['Aluno']

#usando essas fórmulas para o excel, a biblioteca necessita que as fórmulas sejam escritas em inglês
sheet_selecionada['A6'] = '=SUM(A2:A5)'
sheet_selecionada['B6'] = '=B2+B3+B4+B5'
sheet_selecionada['D2'] = '=A2+B2'
sheet_selecionada['D3'] = '=A3-B3'
sheet_selecionada['D4'] = '=A5/B5'





#Salvando as alterações
planilha_que_abrimos_com_python.save(filename=Caminho_arquivo )
print("Processo encerrado")


#Abrindo o arquivo
os.startfile(Caminho_arquivo)