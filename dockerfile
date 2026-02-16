ARG AIRFLOW_VERSION=3.1.7
ARG PYTHON_VERSION=3.10

FROM apache/airflow:${AIRFLOW_VERSION}-python${PYTHON_VERSION}

ENV AIRFLOW_HOME=/opt/airflow

COPY requirements.txt /

RUN pip3 install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt