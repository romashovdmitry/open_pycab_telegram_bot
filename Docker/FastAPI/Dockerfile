FROM python:3.10

WORKDIR /app

ENV TZ=Asia/Baku

COPY ./requirements.txt /app
COPY ./app /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "bot.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
