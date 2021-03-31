FROM python:slim
# COPY api.py /opt/data/api.py
COPY sql_orm.py /opt/data/sql_orm.py
COPY requirements.txt /opt/data/requirements.txt
WORKDIR /opt/data
VOLUME /opt/data
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade pip && pip install paramiko

CMD ["python", "sql_orm.py"]
# CMD ["python", "api.py"]
