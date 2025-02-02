FROM python:3.9

WORKDIR /app

COPY . /app /app

RUN pip install flask_restful flask

EXPOSE 5000

CMD ["python","main.py"]
