FROM python:3.9
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY app /code/app

# Once using docker compose (or any other orchestrator), this last command needs to be removed.
# The orchestrator will start the service once other conditions are met, i.e: database is up.
#CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]