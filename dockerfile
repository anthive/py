FROM python:3.7
COPY . .
EXPOSE 7070
ENTRYPOINT ["python","run.py"]
