FROM python:3.6

RUN mkdir /app
WORKDIR /app

# Intall dependencies
COPY /requirements/development_requirements.txt /app/
COPY /requirements/base_requirements.txt /app/

RUN pip install -r development_requirements.txt
COPY . /app

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
