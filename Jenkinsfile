pipeline {
    agent any

    environment {
        IMAGE_NAME = "employee-app:latest"
        TAR_FILE = "/tmp/employee-app.tar"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Export Docker Image') {
            steps {
                sh '''
                    rm -f ${TAR_FILE}
                    docker save ${IMAGE_NAME} -o ${TAR_FILE}
                '''
            }
        }

        stage('Import Image into K3s') {
            steps {
                sh '''
                    sudo k3s ctr images import ${TAR_FILE}
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    sudo kubectl apply -f k8s/namespace.yaml
                    sudo kubectl apply -f k8s/deployment.yaml
                    sudo kubectl apply -f k8s/service.yaml

                    sudo kubectl rollout restart deployment/employee-app -n employee
                    sudo kubectl rollout status deployment/employee-app -n employee
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sudo kubectl get nodes
                    sudo kubectl get pods -n employee
                    sudo kubectl get svc -n employee
                    sudo kubectl get deployment -n employee
                '''
            }
        }
    }

    post {
        success {
            echo '====================================='
            echo 'Deployment Successful!'
            echo '====================================='
        }

        failure {
            echo '====================================='
            echo 'Deployment Failed!'
            echo '====================================='
        }

        always {
            sh 'rm -f ${TAR_FILE}'
        }
    }
}
