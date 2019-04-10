FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN apk add --no-cache mariadb-dev build-base py-mysqldb
RUN pip install -r requirements.txt
CMD ["python3", "cart.py"]