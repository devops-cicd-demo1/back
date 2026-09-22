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

        stage('Docker Check') {
            steps {
                bat 'docker version'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t devops-demo/backend:1.0 .'
            }
        }
    }
}
