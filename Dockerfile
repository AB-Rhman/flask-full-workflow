FROM python:3.8-slim AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


FROM python:3.8-slim

WORKDIR /app

COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=build /app /app

EXPOSE 5000

ENV FLASK_APP=./src/hello.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]