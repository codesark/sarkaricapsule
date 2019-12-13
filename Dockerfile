FROM python:3.8.0-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib


# install pip dependancies
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./sarkaricapsule .
COPY scap_data.json .


CMD ["sh", "-c", "gunicorn sarkaricapsule.wsgi \
                    --bind 0.0.0.0:8000 \
                    --workers 3"]
