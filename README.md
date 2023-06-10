# Carregamento Google BigQuery

Este programa Python permite executar uma consulta em todas as tabelas de um dataset no Google BigQuery e salvar os resultados em arquivos JSON.

## Pré-requisitos

Antes de executar o programa, certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Pandas

Você também pode instalar as dependências do projeto usando o arquivo `requirements.txt`. Para instalá-las, execute o seguinte comando:
```shell 
pip install -r requirements.txt 
```

## Configuração

Antes de executar o programa, faça o seguinte:

1. Certifique-se de ter um projeto configurado no Google Cloud Platform com acesso ao BigQuery.

2. Faça o download do código-fonte do programa.

## Uso

Para usar o programa, siga estas etapas:

1. Abra um terminal ou prompt de comando.

2. Navegue até o diretório onde o código-fonte do programa está localizado.

3. Execute o seguinte comando:
```python 
python3 index.py
```


Certifique-se de substituir "nome_do_arquivo.py" pelo nome do arquivo em que você salvou o código.

O programa irá:

1. Obter todos os datasets do projeto especificado no BigQuery.

2. Criar uma pasta chamada "outputs" no diretório do programa, se ainda não existir.

3. Para cada dataset, listar todas as tabelas.

4. Executar uma consulta em cada tabela.

5. Gerar um arquivo JSON de saída para cada tabela, armazenado na pasta "outputs".

## Nota

Certifique-se de que o ambiente Python esteja configurado corretamente e as bibliotecas estejam instaladas antes de executar o programa. Verifique se todas as dependências estão instaladas corretamente para evitar erros. Caso prefira, utilize o arquivo `requirements.txt` para instalar as dependências automaticamente.
