pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YogeshEP/employee-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t employee-app:latest .
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker stop employee-container || true
                docker rm employee-container || true

                docker run -d \
                  --name employee-container \
                  -p 5000:5000 \
                  employee-app:latest

                docker ps
                '''
            }
        }
    }
}
