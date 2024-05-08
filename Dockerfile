FROM mariadb:10.6.2

ENV MYSQL_DATABASE=flask_app

COPY db /docker-entrypoint-initdb.d

RUN apt-get update \
    && apt-get -y install python3 python3-pip

WORKDIR /app

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/entrypoint.sh"]
CMD ["-c"]