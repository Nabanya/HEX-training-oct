cat > it_incident_routing_dag.py <<'EOF'
> 
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.standard.operators.python import (
    PythonOperator,
    BranchPythonOperator
)
from airflow.utils.trigger_rule import TriggerRule


# Task 1: Load incident details
def load_incident():
    incident = {
        "ticket_id": "INC-402",
        "service": "Email",
        "severity": "High",
        "reported_by": "Operations"
    }

    return incident


# Task 2: Choose response based on severity
def choose_response(ti):
    incident = ti.xcom_pull(task_ids="load_incident")

    severity = incident["severity"]

    if severity in ["High", "Critical"]:
        print("High priority incident detected!")
        return "urgent_response"
    else:
        print("Normal priority incident detected!")
        return "standard_response"


# Task 3: Handle urgent incidents
    [urgent, standard] >> audit].NONE_FAILED_MIN_ONE_SUCCESS")
> EOF