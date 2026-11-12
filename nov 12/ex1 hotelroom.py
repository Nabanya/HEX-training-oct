cat > hotel_readiness_dag.py <<'EOF'
from datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
# Task 1: Load room details
def load_rooms():
    rooms = [
        {"room": 101, "status": "Ready", "cleaning_min": 0},
        {"room": 102, "status": "Cleaning", "cleaning_min": 25},
        {"room": 103, "status": "Ready", "cleaning_min": 0},
        {"room": 104, "status": "Cleaning", "cleaning_min": 40},
        {"room": 105, "status": "Cleaning", "cleaning_min": 30}
    ]

    return rooms


# Task 2: Find rooms that need cleaning
def find_rooms_to_clean(ti):
    rooms = ti.xcom_pull(task_ids="load_rooms")

    cleaning_rooms = [
        room["room"] for room in rooms
        if room["status"] == "Cleaning"
    ]

    print("Rooms to clean:", cleaning_rooms)

    return cleaning_rooms


# Task 3: Calculate total cleaning time
def calculate_cleaning_minutes(ti):
    rooms = ti.xcom_pull(task_ids="load_rooms")

    [find_cleaning, calculate_time] >> report_reports) EOF