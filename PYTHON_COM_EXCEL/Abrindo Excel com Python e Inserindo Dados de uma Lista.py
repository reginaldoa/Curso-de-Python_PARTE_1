from openpyxl import load_workbook
import os

Caminho_arquivo = 'C:\\Users\\viola\\OneDrive\\Documentos\\CURSOS TECNOLOGIA\\UDEMY\\pythonProject\\PYTHON_COM_EXCEL\\PythonInserindoInformacoesDeLista.xlsx'
planilha_que_abrimos_com_python = load_workbook(filename = Caminho_arquivo)

#Selecionando a planilha e abrindo a mesma
sheet_selecionada = planilha_que_abrimos_com_python ['Aluno']

dados_tabela = [
    ["Time","Seleção",'Idade'],
    ['Palmeiras','Brasil',10],
    ['Milan', 'Itália', 20],
    ['Real Madrid','Espanha',30]
]

#Para ir selecionando a linha que está nos dados_tabela, com o append, vai salvando o que está escrito nelas, na tabela.
for linha_selecionada in dados_tabela:
    sheet_selecionada.append(linha_selecionada)


#Salvando as alterações
planilha_que_abrimos_com_python.save(filename=Caminho_arquivo )
print("Processo encerrado")


#Abrindo o arquivo
os.startfile(Caminho_arquivo)