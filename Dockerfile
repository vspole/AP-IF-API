FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN pip install firebase-admin
RUN pip install google-cloud-firestore
RUN pip install google-auth
COPY ./app /app
