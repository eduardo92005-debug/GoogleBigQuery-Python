from google.oauth2 import service_account
from google.cloud import bigquery


def get_credentials(file = "GBQ_example.json"):
    credentials = service_account.Credentials.from_service_account_file(
    filename=file, scopes=["https://www.googleapis.com/auth/cloud-platform"])
    return credentials

def list_datasets_id(project_id):
    credential = get_credentials()
    client = bigquery.Client(project=project_id, credentials=credential)
    datasets = client.list_datasets()
    datasets_unique = set()
    for dataset in datasets:
        print(dataset.dataset_id)
        datasets_unique.add(dataset.dataset_id)
    return datasets_unique

def list_tables(project_id, dataset_id):
    credential = get_credentials()
    client = bigquery.Client(project=project_id, credentials=credential)
    dataset = client.dataset(dataset_id)
    tables = client.list_tables(dataset)
    tables_unique = set()
    for table in tables:
        tables_unique.add(table.table_id)
        print(table.table_id)
    return tables_unique

def execute_query(project_id, query):
    credential = get_credentials()
    client = bigquery.Client(project=project_id, credentials=credential)
    query_job = client.query(query)
    query_job.result()
    generator = query_job
    return generator