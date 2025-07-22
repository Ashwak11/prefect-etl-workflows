from flow_execution import my_second_flow
from hello_prefect import my_flow  # Import your flow
from etl_prefect import etl_flow
my_second_flow.serve(
    name="my-second-flow",
    parameters={}
)

my_flow.serve(
        name="my-flow",
        parameters={}
    )


etl_flow.serve(
    name="etl-flow",
    parameters={"name":"ETL flow for testing"}
)
