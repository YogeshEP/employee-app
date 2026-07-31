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

        stage('Deploy with Helm') {
            steps {
                sh '''
                    sudo helm upgrade --install employee-app \
                    helm/employee-app \
                    -n employee
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sudo helm list -n employee
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
            echo 'Helm Deployment Successful!'
            echo '====================================='
        }

        failure {
            echo '====================================='
            echo 'Helm Deployment Failed!'
            echo '====================================='
        }

        always {
            sh 'rm -f ${TAR_FILE}'
        }
    }
}
