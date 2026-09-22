pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t devops-demo/backend:1.0 .'
            }
        }

        stage('GHCR Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'github-ghcr',
                    usernameVariable: 'GHCR_USER',
                    passwordVariable: 'GHCR_TOKEN'
                )]) {
                    bat 'echo %GHCR_TOKEN% | docker login ghcr.io -u "%GHCR_USER%" --password-stdin'
                }
            }
        }

        stage('Docker Tag') {
            steps {
                bat 'docker tag devops-demo/backend:1.0 ghcr.io/devops-cicd-demo1/backend:1.0'
            }
        }

        stage('Docker Push') {
            steps {
                bat 'docker push ghcr.io/devops-cicd-demo1/backend:1.0'
            }
                    stage('Deploy') {
            steps {
                bat '''
                    docker pull ghcr.io/devops-cicd-demo1/backend:1.0
                    docker rm -f backend-prod 2>nul
                    docker run -d --name backend-prod -p 5000:5000 ghcr.io/devops-cicd-demo1/backend:1.0
                '''
            }
        }
        }
    }
}