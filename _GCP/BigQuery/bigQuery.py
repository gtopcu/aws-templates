
# https://www.youtube.com/watch?v=2QB4AOJJVes
# pip install google-cloud-bigquery
# pip install google-cloud-bigquery-storage
# pip install db-dtypes # to export to Pandas/Polars

# gcloud init
# gcloud auth application-default login

# bq --help
# bq ls
# bq mk --project_id=project-id --dataset_id=dataset-id --location=location --default_table_expiration=3600
# bq set --project_id=project-id --dataset_id=dataset-id --location=location --default_table_expiration=3600


from google.cloud import bigquery

client = bigquery.Client()
query = """
    SELECT name, SUM(number) as total_people
    FROM `bigquery-public-data.usa_names.usa_1910_2013`
    WHERE state = 'TX'
    GROUP BY name
    ORDER BY total_people DESC
    LIMIT 20
"""

query_job = client.query(query)
# df = query_job.to_dataframe()
# df_pl = query_job.to_arrow() # polars
results = query_job.result()
for row in results:
    print(f"{row.name}: {row.total_people}")

client.close()

# client.query_and_wait()
# client.insert_rows(table, rows_to_insert)
# client.insert_rows_from_dataframe(table, df)
# client.insert_rows_json(table, rows_to_insert)
# client.list_tables()
# client.update_table()
# client.load_table_from_dataframe()
# client.load_table_from_json()
# client.load_table_from_file()
# client.load_table_from_json()
# client.schema_from_json()
# client.schema_to_json()
# client.create_job()
# client.cancel_job()
# client.list_jobs()
# client.create_dataset()
# client.delete_dataset()
# client.delete_table()








