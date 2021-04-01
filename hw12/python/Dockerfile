FROM python:3-slim
COPY db.py /opt/app/db.py
COPY sql_orm.py /opt/app/sql_orm.py
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
VOLUME /opt/app
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --upgrade pip && pip install paramiko

CMD ["python", "sql_orm.py", "logfile.log"]
# ENTRYPOINT ["python", "api.py"]
