#csv:

#cat > atm_cash.csv <<'EOF'
#atm_id,location,cash_available,daily_demand
#ATM101,North,90000,45000
#ATM102,South,25000,40000
#ATM103,East,120000,50000
#ATM104,West,30000,60000
#ATM105,Central,70000,30000
#EOF

#python file:

cat > atm_cash_dag.py <<'EOF'
import csv
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


# Task 1: Load ATM records
def load_atms():
    with open('/opt/airflow/dags/atm_cash.csv', newline='') as file:
        records = list(csv.DictReader(file))

    print("ATM records loaded:", len(records))
    return records


# Task 2: Identify ATMs with low cash
def identify_low_cash(ti):
    records = ti.xcom_pull(task_ids='load_atms')

    low_cash_atms = []

    for atm in records:
        cash = int(atm['cash_available'])
        demand = int(atm['daily_demand'])

        if cash < demand:
            low_cash_atms.append(atm['atm_id'])

    print("Low cash ATMs:", low_cash_atms)

    return low_cash_atms


# Task 3: Calculate total available cash
def calculate_total_cash(ti):
    records = ti.xcom_pull(task_ids='load_atms')

    total_cash = 0

    for atm in records:
        total_cash += int(atm['cash_available'])

    print("Total available cash:", total_cash)

    return total_cash


# Task 4: Generate final report
def generate_report(ti):
    records = ti.xcom_pull(task_ids='load_atms')
    low_cash_atms = ti.xcom_pull(task_ids='identify_low_cash')
    total_cash = ti.xcom_pull(task_ids='calculate_total_cash')

    print("========== ATM CASH REPLENISHMENT REPORT ==========")
    print("Total number of ATMs:", len(records))
    print("ATMs requiring cash replenishment:", low_cash_atms)
    print("Total available cash: Rs.", total_cash)
    print("===================================================")


# Define the DAG
with DAG(
    dag_id='atm_cash_pipeline',
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    load_task = PythonOperator(
        task_id='load_atms',
        python_callable=load_atms
    )

    low_cash_task = PythonOperator(
        task_id='identify_low_cash',
        python_callable=identify_low_cash
    )

    total_cash_task = PythonOperator(
        task_id='calculate_total_cash',
        python_callable=calculate_total_cash
    )

    report_task = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )

    load_task >> [low_cash_task, total_cash_task] >> report_task

EOF