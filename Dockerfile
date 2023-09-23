FROM python:3.11.4
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
RUN pip3 install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install
RUN pipenv install --system --deploy --ignore-pipfile
COPY . .
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
# docker build -t ver_02 .
# docker run -p 8000:8000 ver_02
# CTRL + C  // Остановить