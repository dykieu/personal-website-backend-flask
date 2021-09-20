FROM python:latest

RUN mkdir -p /test/

WORKDIR /test/

COPY requirements.txt /test/

RUN pip install -r requirements.txt

COPY . /test/

ENV FLASK_APP="application:create_app()"
ENV FLASK_ENV="development"

ENTRYPOINT [ "gunicorn" ]

CMD [ "-b", ":5000" , "--access-logfile", "-" , "application:create_app()"]