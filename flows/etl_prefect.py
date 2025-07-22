from prefect import task, flow
import requests
from pymongo import MongoClient

# Extract Task
@task(retries=3)
def extract():
    url = "https://jsonplaceholder.typicode.com/posts" #url from where we fetch data
    response = requests.get(url)
    data = response.json()  # Corrected to call json() to parse the response
    return data

# Transform Task
@task
def transform(data):
    # Transforming data to extract titles
    transformed_data = [{"title": item['title']} for item in data]  # Ensure each item is a dict
    return transformed_data

# Load Task
@task
def load(transformed_data):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["database_name"]  # Database name
    collection = db["Collection_name"]  # Collection name

    # Insert transformed data into MongoDB
    # Insert many documents at once
    collection.insert_many(transformed_data)

    print(f"Successfully inserted {len(transformed_data)} documents into MongoDB")

# Flow that links all tasks together
@flow
def etl_flow(name="ETL flow for testing"):
    # Calling extract and await its result
    data = extract()  # This will fetch the data asynchronously
    
    # Calling transform and awaiting its result
    transformed_data = transform(data)  # The data from extract is passed here and transformed
    
    # Calling load and awaiting its result
    load(transformed_data)  # The transformed data is passed here for loading

if __name__ == "__main__":
    etl_flow()
