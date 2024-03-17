FROM python:3.8
LABEL maintainer="Oscar Garcia"

COPY ./src  /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
# command to run on container start
CMD [ "python", "app.py" ]