#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 3),
    'depends_on_past': False,
}
with DAG(
    'mydag',
    default_args=default_args,
    schedule_interval='@once',
    catchup=False
) as dag:
    
    t1 = BashOperator(
        task_id='bash_good_morning',
        dag=dag,
        bash_command='echo "Good morning my diggers!"'
)

