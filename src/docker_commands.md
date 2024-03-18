## Docker commands used to build the application
```shell
docker build -t codepoetme/techtrends:v1 .
```

## Docker commands used to run the application
```shell
docker run -p 30007:3111 codepoetme/techtrends:v1
```

## Docker commands used to get the application logs
```shell
docker logs -f <container_id>
```

## Logs from the container running the TechTrends application
```shell
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:3111/ (Press CTRL+C to quit)
172.17.0.1 - - [17/Mar/2024 10:05:20] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [17/Mar/2024 10:05:20] "GET /static/css/main.css HTTP/1.1" 200 -
172.17.0.1 - - [17/Mar/2024 10:05:21] "GET /favicon.ico HTTP/1.1" 404 -
172.17.0.1 - - [17/Mar/2024 10:05:23] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [17/Mar/2024 10:05:23] "GET /static/css/main.css HTTP/1.1" 304 -
Creating a post... 
172.17.0.1 - - [17/Mar/2024 10:05:27] "GET /create HTTP/1.1" 200 -
172.17.0.1 - - [17/Mar/2024 10:05:27] "GET /static/css/main.css HTTP/1.1" 304 -
Creating a post... 
172.17.0.1 - - [17/Mar/2024 10:05:33] "POST /create HTTP/1.1" 302 -
172.17.0.1 - - [17/Mar/2024 10:05:33] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [17/Mar/2024 10:05:33] "GET /static/css/main.css HTTP/1.1" 304 -


```