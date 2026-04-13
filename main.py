Create a repository in GIT and create the following files:
• index.html
• Dockerfile
• Deployment.yaml


Create index.html:
<!DOCTYPE html>
<html>
<head>
<title>CI/CD Demo</title>
<style>
body{
text-align:center;
font-family:Times New Roman;
background-color:#af0d0d;
}
h1{
color:#0ef777;
}
</style>
</head>
<body>
<h1>CI/CD Pipeline Working</h1>
<h2>Deployed using Jenkins + Docker + Kubernetes</h2>
<p>This webpage is automatically deployed using a CI/CD pipeline.</p>
</body>
</html>


Create a Dockerfile
FROM nginx:latest
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80


deployment.yaml:
apiVersion: apps/v1
kind: Deployment
metadata:
 name: labfat
spec:
 replicas: 2
 selector:
  matchLabels:
   app: labfat
 template:
  metadata:
   labels:
    app: labfat
  spec:
   containers:
   - name: labfat
     image: 23mis0239/labfat:latest
     ports:
     - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
 name: html-demo-service
spec:
 type: NodePort
 selector:
  app: labfat
 ports:
 - port: 80
   targetPort: 80
   nodePort: 30010

3. Open Jenkins
In Jenkins Setting --> Credentials
New Credentials – User name: <should use the Docker Desktop username>, password <same as,,,,,,,docker name and password of it id is dockerhub
Docker Desktop password>, ID:<dockerhub>, Description <any>

New Credentials – Secret – Broswse C: User->Administrator-->.kube id:kuberconfig

4.jenkins pipeline script:
  pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "23mis0239/labfat"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Abi503/labfat.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub',
                usernameVariable: 'USER', passwordVariable: 'PASS')]) {

                    bat 'docker login -u %USER% -p %PASS%'
                    bat 'docker push %DOCKER_IMAGE%'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kuberconfig', variable: 'KUBECONFIG')]) {

                    bat '''
                    set KUBECONFIG=%KUBECONFIG%
                    kubectl apply -f deployment.yaml
                    kubectl apply -f service.yaml
                    '''
                }
            }
        }

    }
}

kubectl get all in command prompt
  localhost:30010
