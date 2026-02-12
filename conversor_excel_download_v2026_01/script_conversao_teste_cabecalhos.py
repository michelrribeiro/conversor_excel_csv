import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('future.no_silent_downcasting', True)
from pathlib import Path
import os

# Caminho raiz da pasta onde estão os arquivos:
entrada = r"./in/"

def exec_conv(in_path):

	filesList = []
	fileNames = []
	dfCabecalhos = pd.DataFrame()	
	fullPath = []
	status = []

	# Populando a lista de arquivos:
	for currentpath, folders, files in os.walk(in_path):
	    for file in files:
	        filesList.append(os.path.join(currentpath, file))

	filesCount = len(filesList)
	convCount = 0

	# Mapeamento das extensões possíveis:
	engine_map = {'xlsx': 'openpyxl', 'xlsm': 'openpyxl', 'xlsb': 'pyxlsb', 'xls': 'xlrd'}

	# Convertendo arquivos:
	for file in filesList:

		try:
			engine = engine_map.get(file.split('.')[-1].lower())
			readFile = pd.ExcelFile(file, engine=engine)

			for sheet in readFile.sheet_names:
				df = pd.read_excel(file, engine=engine, sheet_name=sheet, dtype='str', header=None)
				df = df.replace(r'\s+', ' ', regex=True).replace(r'\"\'\|', ' ', regex=True)
				df['FileName'] = file.replace('./in/', '').replace(file.split('.')[-1], '')+'_'+sheet
				df.loc[0, 'FileName'] = 'FileName'
				df['dttLinha'] = [str(n+1) if n != 0 else 'dttLinha' for n in df.index.tolist()]
				df.to_csv('./out/'+file.split('\\')[-1].replace('./in/', '').replace(file.split('.')[-1], '')+'_'+sheet+'_utf_8.csv', sep='|', index=False, encoding='utf-8')
				dfCabecalhos = pd.concat([dfCabecalhos, df.head(15)], ignore_index=True)

			fullPath.append(file)
			status.append('1')
			convCount = convCount+1
			print('Convertidos', str(convCount), 'de', str(filesCount))

		except Exception as e:
			print(f'Erro no arquivo {file}, incluindo o erro: {e}')
			fullPath.append(file)
			status.append('0')

	# Exportar a lista de arquivos convertidos:
	dfPath = pd.DataFrame({'FullPath': fullPath, 'Status': status})
	dfPath.to_excel('./status_arquivos.xlsx', index=False)

	# Exportar os cabeçalhos dos arquivos convertidos:
	dfCabecalhos.to_excel('./cabecalhos_convertidos.xlsx', index=False)

if __name__ == '__main__':
	exec_conv(entrada)