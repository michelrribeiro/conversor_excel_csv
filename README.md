#### Pré-requisitos:
+ python3;
+ bibliotecas definidas no arquivo de requirements.

#### Conteúdo da pasta "conversor_excel_download_v2026_01":
+ pasta /in/: pasta para receber os arquivos de excel a serem convertidos;
+ pasta /out/: pasta de destino dos arquivos convertidos para csv sendo um arquivo para cada planilha/aba em cada pasta de trabalho do excel;
+ 0_venv_primeiro_uso_bat: executável para a criação de ambiente virtual python;
+ 1_script_conversao_teste_cabecalhos.bat: executável que chama o script de conversão dos arquivos;
+ 2_script_consolidacao.bat: executável que chama o script de consolidação dos arquivos convertidos com base no cabeçalho de cada um;
+ script_conversao_teste_cabecalhos.py: script python que converte os arquivos aplicando regex para remover tab, enter e o delimitador usado ao final (\s+ e |);
+ script_consolidacao.py: script python que consolida os arquivos convertidos;
+ requirements.txt: lista de bibliotecas necessárias com suas respectivas versões.

#### Mode de utilizar:
1) Criar o ambiente virtual python manualmente ou através do executável. Para o projeto de teste foi utilizado python3 a partir da Microsoft Store, o que dribla falta de permissões para instalar python em máquinas corporativas e, conforme pode ser visto ao abrir o arquivo 0.bat com um editor de texto, o caminho para o python3 está na variável %PYTHON%;
2) Após a criação do ambiente virtual e transferência dos arquivos de interesse para a pasta 1, executar o arquivo 1.bat para a conversão, o que pode levar algum tempo a depender dos arquivos, mas não demanda passos adicionais ou supervisão;
3) Avaliar o arquivo de cabeçalhos convertidos para verificar se todos os arquivos convertidos são de interesse e se possuem o mesmo schema com os mesmos nomes de cabeçalho e, após organizar os arquivos a serem consolidados na pasta out, executar o arquivo 2.bat, que consolida os arquivos e retorna o arquivo excel_consolidado.csv na pasta raiz.
