
# Docker and Kubernetes Activity

## Project Overview
This project demonstrates the containerization and deployment of a Python Flask web application using Docker and Kubernetes.

## Technologies Used
- Python
- Flask
- Docker
- Kubernetes
- kubectl

## Project Structure
```text
Assignment-Docker-Kubernetes/
├── app.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── .gitignore
└── README.md
```

## Application Features
- Flask web application
- Homepage displaying a welcome message
- Health check endpoint at /health
- Docker containerization
- Kubernetes Deployment with 2 replicas
- Kubernetes NodePort Service

## Run Locally
Install dependencies:
```bash
pip install -r requirements.txt
```

Run:
```bash
python app.py
```

Access: http://localhost:5000

## Docker Instructions
Build the image:
```bash
docker build -t docker-kubernetes-activity:v1 .
```

Run the container:
```bash
docker run -d --name flask-demo -p 5000:5000 docker-kubernetes-activity:v1
```

Access: http://localhost:5000

## Kubernetes Deployment
Apply Deployment:
```bash
kubectl apply -f deployment.yaml
```

Apply Service:
```bash
kubectl apply -f service.yaml
```

Check Pods:
```bash
kubectl get pods
```

Check Deployment:
```bash
kubectl get deployments
```

Check Service:
```bash
kubectl get services
```

## Access the Application
Homepage: http://localhost:30007

Health Check: http://localhost:30007/health

## Author
Prajwal Jadhav
