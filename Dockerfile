# Dockerfile

FROM python:3.9-slim

WORKDIR /app

COPY ./yodafy.py /app/yodafy.py

RUN chmod +x yodafy.py

ENTRYPOINT ["python", "yodafy.py"]
