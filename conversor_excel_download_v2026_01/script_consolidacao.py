import pandas as pd
import os
from pathlib import Path
import shutil

# Caminho raiz da pasta onde estão os arquivos:
saida = r"./out/"

def exec_cons(out_path):

	consolidar = input('''\nO processo concatenará apenas colunas com nomes idênticos independentemente da ordem das colunas, o que pode gerar resultados não esperados caso haja, por exemplo, colunas conta e account_number em diferentes arquivos. Por favor verifique que apenas os arquivos de interesse estão dentro da pasta /arquivos.\nDigite S para consolidar os arquivos.\n''')

	if consolidar.lower() == 's':
		filesList = []
		fileNames = []

		# Populando a lista de arquivos:
		for currentpath, folders, files in os.walk(out_path):
			for file in files:
				filesList.append(os.path.join(currentpath, file))

		# Segregando os arquivos csv:
		csvList = [item.replace('\\', '/') for item in filesList if item[-3:].lower() == 'csv']
		
		# Consolidando os arquivos:
		if len(csvList) > 0:
			# Primeiro dataframe para servir de base para o resto:
			finalTable = pd.read_csv(csvList[0], sep='|', dtype='str', encoding='utf-8', header=1)
			finalTable.columns = [col.strip() for col in finalTable.columns]

			# Concatenando demais arquivos:
			for file in csvList[1:]:
				df = pd.read_csv(file, sep='|', dtype='str', header=1)
				df.columns = [col.strip() for col in df.columns]

				finalTable = pd.concat([finalTable, df], axis=0, ignore_index=True)
				print('Concatenados', str(csvList.index(file)+1), 'de', str(len(csvList)))

			# Exportando o consolidado:
			finalTable.to_csv('./excel_consolidado_utf_8.csv', sep='|', index=False, encoding='utf-8')

if __name__ == '__main__':
	exec_cons(saida)