FROM python:3.9
ENV PYTHONUNBUNFFERED 1
RUN  mkdir /code
WORKDIR /code
COPY . /code
RUN apt-get update && apt-get install -y --no-install-recommends \
    unixodbc-dev \
    unixodbc \
    libpq-dev \
    wkhtmltopdf
RUN python -m pip install -r requirements.txt

