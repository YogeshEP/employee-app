pipeline {
    agent any

    environment {
        IMAGE_NAME = "employee-app:latest"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t ${IMAGE_NAME} .
                '''
            }
        }

        stage('Export Docker Image') {
            steps {
                sh '''
                docker save ${IMAGE_NAME} -o k8s/employee-app.tar
                '''
            }
        }

        stage('Import Image into K3s') {
            steps {
                sh '''
                sudo k3s ctr images import k8s/employee-app.tar
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/namespace.yaml
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                kubectl rollout restart deployment employee-app -n employee
                kubectl rollout status deployment employee-app -n employee
                '''
            }
        }
    }

    post {
        success {
            echo "Deployment completed successfully!"
        }

        failure {
            echo "Deployment failed!"
        }
    }
}
