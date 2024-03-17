# How to deploy Helm chart

## Step 1 - Test helm templates for errors
 - cd <helm dir>
 - helm template techtrends . --debug
 - helm install techtrends . -- dry-run

## Step 2 - Install helm chart
- cd <helm dir>
- helm install techtrends .


## Step 3 - Expose service
```shell
k3d cluster edit mycluster --port-add 3111:30007@server:0
```

## Step 4 - Uninstall helm chart
- helm uninstall techtrends 
