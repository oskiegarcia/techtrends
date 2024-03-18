## Docker commands used to build the application
```shell
docker build -t codepoetme/techtrends:v3 .
```

## Docker commands used to run the application
```shell
docker run -d -p 7111:3111 codepoetme/techtrends:v3 
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
WARNING:_internal:18/03/2024 05:23:22,  * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
INFO:_internal:18/03/2024 05:23:22,  * Running on http://172.17.0.2:3111/ (Press CTRL+C to quit)
INFO:_internal:18/03/2024 05:24:55, 172.17.0.1 - - [18/Mar/2024 05:24:55] "GET / HTTP/1.1" 200 -
INFO:_internal:18/03/2024 05:24:55, 172.17.0.1 - - [18/Mar/2024 05:24:55] "GET /static/css/main.css HTTP/1.1" 304 -
INFO:app:18/03/2024 05:25:07, Article "2020 CNCF Annual Report" retrieved!
INFO:_internal:18/03/2024 05:25:07, 172.17.0.1 - - [18/Mar/2024 05:25:07] "GET /1 HTTP/1.1" 200 -
INFO:_internal:18/03/2024 05:25:07, 172.17.0.1 - - [18/Mar/2024 05:25:07] "GET /static/css/main.css HTTP/1.1" 304 -
Creating a post... 
INFO:_internal:18/03/2024 05:25:15, 172.17.0.1 - - [18/Mar/2024 05:25:15] "GET /create HTTP/1.1" 200 -
INFO:_internal:18/03/2024 05:25:15, 172.17.0.1 - - [18/Mar/2024 05:25:15] "GET /static/css/main.css HTTP/1.1" 304 -
Creating a post... 
INFO:_internal:18/03/2024 05:25:31, 172.17.0.1 - - [18/Mar/2024 05:25:31] "POST /create HTTP/1.1" 302 -
INFO:_internal:18/03/2024 05:25:31, 172.17.0.1 - - [18/Mar/2024 05:25:31] "GET / HTTP/1.1" 200 -
INFO:_internal:18/03/2024 05:25:31, 172.17.0.1 - - [18/Mar/2024 05:25:31] "GET /static/css/main.css HTTP/1.1" 304 -
INFO:app:18/03/2024 05:25:49, Metrics request successfull
INFO:_internal:18/03/2024 05:25:49, 172.17.0.1 - - [18/Mar/2024 05:25:49] "GET /metrics HTTP/1.1" 200 -
INFO:app:18/03/2024 05:26:01, Status request successfull
INFO:_internal:18/03/2024 05:26:01, 172.17.0.1 - - [18/Mar/2024 05:26:01] "GET /healthz HTTP/1.1" 200 -
INFO:app:18/03/2024 05:26:31, Status request successfull
INFO:_internal:18/03/2024 05:26:31, 172.17.0.1 - - [18/Mar/2024 05:26:31] "GET /healthz HTTP/1.1" 200 -
```