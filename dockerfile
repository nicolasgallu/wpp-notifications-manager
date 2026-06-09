FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y tzdata \
    && rm -rf /var/lib/apt/lists/*
ENV TZ=America/Argentina/Buenos_Aires
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "2", "--worker-class", "gthread", "--timeout", "300", "main:app"]