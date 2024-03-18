# ArgoCD

## How to install ArgoCD

### Step 1 - Install ArgoCD on kubernetes cluster
```shell
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

### Step 2 - Install AgoCD CLI
```shell
brew install argocd
```
	 

### Step 3 - Enable Port Forwarding
```shell
kubectl port-forward svc/argocd-server -n argocd 8080:443
```
Alternatively, we can also create a nodeport
https://github.com/udacity/nd064_course_1/blob/main/solutions/argocd/argocd-server-nodeport.yaml

### Step 4 - Get initial password for user admin
```shell
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

Alternatively, we can you the argocd CLI command
```shell
argocd admin initial-password -n argocd
```

Step 4 - Access ArgoCD UI and update password
https://localhost:8080/applications 

Step 5 - Delete secret for initial admin password
```shell
kubectl delete secret argocd-initial-admin-secret -n argocd
```

Step 6 - Create ArgoCD applications
```shell
kubectl apply -f helm-techtrends-sandbox.yaml
kubectl apply -f helm-techtrends-staging.yaml
kubectl apply -f helm-techtrends-prod.yaml
```
