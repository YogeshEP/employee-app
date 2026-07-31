pipeline {
    agent any

    environment {
        IMAGE_NAME = "employee-app:latest"
        IMAGE_TAR = "/tmp/employee-app.tar"
        NAMESPACE = "employee"
        RELEASE_NAME = "employee-app"
        HELM_CHART = "helm/employee-app"
        KUBECONFIG = "/var/lib/jenkins/.kube/config"
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
                rm -f ${IMAGE_TAR}
                docker save ${IMAGE_NAME} -o ${IMAGE_TAR}
                '''
            }
        }

        stage('Import Image into K3s') {
            steps {
                sh '''
                sudo k3s ctr images import ${IMAGE_TAR}
                '''
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh '''
                sudo env KUBECONFIG=${KUBECONFIG} \
                /usr/local/bin/helm upgrade --install ${RELEASE_NAME} \
                ${HELM_CHART} \
                -n ${NAMESPACE}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "=============================="
                echo "Helm Releases"
                echo "=============================="

                sudo env KUBECONFIG=${KUBECONFIG} \
                /usr/local/bin/helm list -n ${NAMESPACE}

                echo ""
                echo "=============================="
                echo "Pods"
                echo "=============================="

                sudo kubectl get pods -n ${NAMESPACE}

                echo ""
                echo "=============================="
                echo "Services"
                echo "=============================="

                sudo kubectl get svc -n ${NAMESPACE}

                echo ""
                echo "=============================="
                echo "Deployments"
                echo "=============================="

                sudo kubectl get deployment -n ${NAMESPACE}
                '''
            }
        }
    }

    post {

        always {
            sh '''
            rm -f ${IMAGE_TAR}
            '''
        }

        success {
            echo '====================================='
            echo 'CI/CD Pipeline Completed Successfully!'
            echo 'Application Deployed using Helm'
            echo '====================================='
        }

        failure {
            echo '====================================='
            echo 'Helm Deployment Failed!'
            echo '====================================='
        }
    }
}
