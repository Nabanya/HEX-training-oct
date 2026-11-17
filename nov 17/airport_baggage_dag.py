#csv file:

#cat > airport_baggage.csv <<'EOF'
#bag_id,flight_no,weight_kg,screening_status
#BG101,AI502,18,Clear
#BG102,AI502,27,Clear
#BG103,6E214,12,Review
#BG104,6E214,22,Clear
#BG105,UK812,25,Review
#BG106,UK812,15,Clear
#EOF

#python file:

cat > airport_baggage_dag.py <<'EOF'
import csv
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


# Task 1: Load baggage records
def load_baggage():
    with open('/opt/airflow/dags/airport_baggage.csv', newline='') as file:
        records = list(csv.DictReader(file))

    print("Baggage records loaded:", len(records))
    return records


# Task 2: Identify bags requiring manual review
def identify_review_bags(ti):
    records = ti.xcom_pull(task_ids='load_baggage')

    review_bags = []

    for bag in records:
        weight = int(bag['weight_kg'])
        status = bag['screening_status']

        if status == 'Review' or weight > 23:
            review_bags.append(bag['bag_id'])

    print("Bags requiring manual review:", review_bags)

    return review_bags


# Task 3: Calculate total baggage weight
def calculate_total_weight(ti):
    records = ti.xcom_pull(task_ids='load_baggage')

    total_weight = 0

    for bag in records:
        total_weight += int(bag['weight_kg'])

    print("Total baggage weight:", total_weight, "kg")

    return total_weight


# Task 4: Generate final report
def generate_report(ti):
    records = ti.xcom_pull(task_ids='load_baggage')
    review_bags = ti.xcom_pull(task_ids='identify_review_bags')
    total_weight = ti.xcom_pull(task_ids='calculate_total_weight')

    print("========== AIRPORT BAGGAGE SCREENING REPORT ==========")
    print("Total number of bags:", len(records))
    print("Bags requiring manual review:", review_bags)
    print("Total baggage weight:", total_weight, "kg")
    print("======================================================")


# Define the DAG
with DAG(
    dag_id='airport_baggage_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    load_task = PythonOperator(
        task_id='load_baggage',
        python_callable=load_baggage
    )

    review_task = PythonOperator(
        task_id='identify_review_bags',
        python_callable=identify_review_bags
    )

    weight_task = PythonOperator(
        task_id='calculate_total_weight',
        python_callable=calculate_total_weight
    )

    report_task = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )

    load_task >> [review_task, weight_task] >> report_task

EOF