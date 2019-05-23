FROM python:3-alpine

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN chmod +x boot.sh

#EXPOSE 5000
#ENTRYPOINT ["sh", "boot.sh"]
#CMD gunicorn --bind 0.0.0.0:$PORT manage:app