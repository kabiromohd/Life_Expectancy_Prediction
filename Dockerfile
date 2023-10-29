FROM python:3.11-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "model_rf_1.pkl", "model_dv.pkl", "./"]

EXPOSE 9690

ENTRYPOINT ["pipenv", "run", "gunicorn", "--bind=0.0.0.0:9690", "predict:app"]