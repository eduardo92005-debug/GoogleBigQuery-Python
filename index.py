## carregamento Google Big_query
import pandas as pd
import helper_gbq
import os
import shutil

PROJECT_ID = "meu-projeto-g3"

def cria_pasta_outputs():
    output_folder = 'outputs'
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
        os.makedirs(output_folder)
    else:
        os.makedirs(output_folder)
    return output_folder
    
def executa_query_em_todas_tabelas_de_um_dataset():
    # Lista todos os datasets dado um projeto especifico
    print("Obtendo todos os datasets...")
    datasets = helper_gbq.list_datasets_id(PROJECT_ID)
    print("Feito! Criando pasta de outputs...")
    output_name = cria_pasta_outputs()
    print("Obtendo todas as tabelas dos datasets...")
    for dataset in datasets:
        print(f"Dataset: {dataset}")
        # Lista todas as tabelas de um dataset especifico
        print("Tabelas: ")
        tables = helper_gbq.list_tables(PROJECT_ID,dataset)
        for table in tables:
            print(f"Executando query na tabela {table}, aguarde...")
            query = f"SELECT * FROM {PROJECT_ID}.{dataset}.{table}"
            # Executa query
            results = helper_gbq.execute_query(PROJECT_ID,query)
            # Obtem os resultados da query
            result = [dict(row) for row in results]
            print("Gerando output...")
            df = pd.DataFrame(result)
            output_file = os.path.join(output_name, f'output_{table}.json')
            df.to_json(output_file, orient='records')
            print("Sucesso!")
            
                
                

executa_query_em_todas_tabelas_de_um_dataset()



