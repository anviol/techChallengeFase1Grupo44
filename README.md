# Tech Challenge Fase 1 Grupo 44
Trabalho em grupo do curso de analise da dados da Fiap

# Trabalhando a apresentação com o Stream Lite, no VS Code, no Windows

Instalação baseada na documentação [Docs Streamlit](https://docs.streamlit.io/get-started/installation/anaconda-distribution)

## Passo 1: Instalar o Anaconda

1. Baixe o Anaconda do [site oficial](https://www.anaconda.com/products/individual).
2. Execute o instalador e siga as instruções, prestando atenção às opções de adicionar o Anaconda ao seu PATH (recomenda-se geralmente não adicionar ao PATH pelo instalador, mas o VS Code precisa disso).
3. Uma vez instalado, abra o Anaconda Navigator para facilitar a gestão dos ambientes e pacotes.

## Passo 2: Criar um Ambiente Conda

### Dentro do Anaconda Navigator:

1. Vá para a aba "Environments".
2. Clique em "Create" na parte inferior do menu de ambientes.
3. Dê um nome ao seu ambiente, selecione a versão do Python e clique em "Create".

### Via linha de comando:

```bash
conda create -n techChallengeFase1Grupo44 python=3.11.9 pandas=2.2.1 chardet=4.0.0 streamlit=1.32.0 jupyter=7.0.8
conda activate techChallengeFase1Grupo44
```

### Passo 3: Instalar Pacotes no Ambiente

## Anaconda Navigator:

1. Ative o ambiente criado, selecionando-o.
2. Mude para a aba "Home" e escolha "Open Terminal" ou "Open with Jupyter Notebook" se preferir uma interface de notebook.

### Via linha de comando:

```bash
conda install [PACOTE]
conda install -c conda-forge [PACOTE]
```
>**Observação**: Por enquanto instalamos todos os pacotes no momento da criaçao, não precisa executar esses comandos, mas vou deixa-los de exemplo.

### Passo 4: Instalar o VS Code (Se ainda não estiver instalado)

1. Baixe e instale o VS Code do [site oficial](https://code.visualstudio.com/).
2. Abra o VS Code após a instalação.

### Passo 5: Instalar a Extensão do Python para o VS Code

1. No VS Code, vá para a aba de extensões (o ícone da caixa quadrada ou use o atalho `Ctrl+Shift+X`).
2. Procure por "Python" e instale a extensão oficial da Microsoft.

### Passo 6: Configurar o VS Code para Usar o Ambiente Conda

1. Abra o VS Code e crie ou abra um arquivo Python.
2. Na barra de status na parte inferior, clique no interpretador Python atual.
3. Uma lista de interpretadores Python disponíveis aparecerá. Escolha o ambiente Conda que você criou.

Depois disso, o interpretador selecionado será usado para executar scripts Python dentro do VS Code.

### Passo 7: Biblioteca Stramlit

```bash
conda install -c conda-forge streamlit
```

Para verificar se funcionou de o comando:

```bash
streamlit hello
```
### Passo 8: Complementos VS Code

Instale os complementos

- Python (Microsoft)
- Pylance (Microsoft)
- Jupyter Notebook (Microsoft)

### Executando

```bash
streamlit run .\src\tech_challenge.py
```

Para que atualize a cada alteração salva basta clicar em "Always rerun" na tela do navegador após a primeira modificação no arquivo. 