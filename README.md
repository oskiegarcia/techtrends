# TechTrends Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Run

To run this application there are a few steps required:

1. change directory to src
```shell
cd src
```
1. Install dependencies 
```shell
pip install -r requirements.txt
```

2. Initialize the database
```shell
python init_db.py
```
This will create or overwrite the `database.db` file that is used by the web application.

4. Run the TechTrends application.
```shell
python app.py
````
The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.