import streamlit as st
import pandas as pd
import chardet

anos_analisados = list(range(2008, 2023))

st.markdown('# Tech Challenge - Grupo 44')

st.markdown('## O Problema')
st.markdown('Imagine agora, que você vai atuar como Expert em Data Analytics em uma empresa que exporta vinhos do Brasil para o mundo todo.')
st.markdown('Sua área é recém-criada dentro da empresa, e você será responsável pelos relatórios iniciais a serem apresentados em uma reunião de investidores e acionistas, explicando a quantidade de vinhos exportados e os fatores externos que podem vir a surgir e que interferem nas análises:')
st.markdown('1. Dados climáticos;')
st.markdown('2. Dados demográficos;')
st.markdown('3. Dados econômicos;')
st.markdown('4. Dados de avaliações de vinhos.')

st.markdown('O Head de Dados pediu para que você construísse uma tabela contendo as seguintes informações:')

st.markdown('a. País de origem (Brasil);')
st.markdown('b. País de destino;')
st.markdown('c. Quantidade em litros de vinho exportado (utilize: 1KG =1L);')
st.markdown('d. Valor em US$;')

st.markdown('Os dados que lhe forneceram são de uma vinícola parceira, e podem ser encontrados [aqui](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01).')

st.markdown('## Objetivo')

st.markdown('Seu objetivo é dizer o montante de venda de exportação nos últimos 15 anos, separando a análise por país e trazendo quais as prospecções futuras e possíveis ações para uma melhoria nas exportações. Construa gráficos atraentes e que passem a ideia central para que os acionistas e investidores possam seguir em frente com suas ações.')

st.markdown('>**DICA**: Para construir uma boa análise, utilize várias bases do mesmo site! Outro ponto interessante, é utilizar os dados externos citados acima para enriquecer ainda mais a mensagem que você quer passar.')

st.markdown('Lembre-se de que você poderá apresentar o desenvolvimento do seu projeto durante as lives com docentes no Discord! Essa é uma boa oportunidade para discutir sobre as dificuldades encontradas e pegar dicas valiosas com especialistas e colegas de turma.')

st.markdown('>**IMPORTANTE**: Não esqueça de que este é um entregável obrigatório! Se atente para o prazo de entrega até o final da fase!')

csv_vitibrasil_producao = pd.read_csv('./dados_originais/embrapa/Producao.csv', sep=";")
csv_vitibrasil_comercio = pd.read_csv('./dados_originais/embrapa/Comercio.csv', sep=";")
csv_vitibrasil_exportacao = pd.read_csv('./dados_originais/embrapa/ExpVinho.csv', sep=";")
csv_vitibrasil_importacao = pd.read_csv('./dados_originais/embrapa/ImpVinhos.csv', sep=";")
csv_vitibrasil_processamento = pd.read_csv('./dados_originais/embrapa/ProcessaViniferas.csv', sep=";")

def importacao_dados_inmet(csv_file_path : str):

  with open (csv_file_path, "rb") as file:
    bytes = file.read(100)

  encoding_file = chardet.detect(bytes)

  if encoding_file.get("encoding") == 'ascii':
    encoding_file = 'ISO-8859-1'
  else:
    encoding_file = encoding_file.get("encoding")

  return pd.read_csv(csv_file_path
                              , sep=";"
                              , encoding=encoding_file
                              , skiprows=8)

csv_inmet_por_ano = {}

for ano in anos_analisados:
  csv_inmet_por_ano[ano] = importacao_dados_inmet(f'./dados_originais/INMET/INMET_S_RS_A840_BENTO GONCALVES_01-01-{ano}_A_31-12-{ano}.CSV')

st.dataframe(csv_inmet_por_ano[2020])

tabela_descritiva = csv_inmet_por_ano[2020].T

st.table(tabela_descritiva)