pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t remote-patient-monitoring .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker stop remote-patient-container || exit 0'
                bat 'docker rm remote-patient-container || exit 0'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name remote-patient-container remote-patient-monitoring'
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}