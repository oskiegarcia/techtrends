FROM python:2.7
LABEL maintainer="Oscar Garcia"

COPY ./src  /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements-2.7.txt

ENV PYTHONUNBUFFERED=1

RUN python init_db.py

EXPOSE 3111

# command to run on container start
CMD [ "python", "app.py" ]