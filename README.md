# TechTrends Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Note: k3d instead of Vagrant + Virtualbox + k3s
For some reason, I am not able to successfully run Virtualbox and Vagrant on my mac machine.
Therefore, I have used k3d instead - it is a lightweight wrapper to run k3s. See https://k3d.io/v5.6.0/.

The following are the steps to install on mac machine:
### Step 1 - Ensure Docker is up and running, then launch your terminal and run the command below:
```shell
brew install k3d
k3d version
```

### Step 1 - Provision k3s cluster mapping the port 30007 from agent-0 to localhost:3111 
```shell
k3d cluster create mycluster -p "3111:30007@agent:0" --agents 2
```
The port mapping allows us to access the application on http://localhost:3111



## Run (Using python commands)

To run this application there are a few steps required:

1. change directory to src and activate virtual environment
```shell
cd src
. venv/bin/activate
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

## Run (Using docker commands)

1. Build the application
```shell
docker build -t codepoetme/techtrends:v1 .
```

2. Run the application
```shell
docker run -p 30007:3111 cosdepoetme/techtrends:v1
```
3. Open in the browser http://localhost:30007


## Run/Deploy (Using helm commands)
1. Deploy
```shell
cd helm/techtrends
helm install techtrends .
```

2. Open in the browser http://localhost:3111

## Run/Deploy (Using ArgoCD)
1. Create ArgoCD application
```shell
cd argocd
kubectl apply -f argocd-deploy.yaml
```
2. Open the ArgoCD application on the UI and sync in order to deploy techtrends application on kubernetes cluster.

3. Open in the browser http://localhost:3111


