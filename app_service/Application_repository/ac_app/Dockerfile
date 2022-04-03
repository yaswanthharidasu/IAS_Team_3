FROM python:3.8-slim-buster
WORKDIR /ac_app
RUN pip3 install -r /var/www/requirements.txt
COPY . .
COPY ../../../api.py .
EXPOSE 6001
CMD ["python3","-m","flask","run"]
COPY ./requirements.txt /var/www/requirements.txt