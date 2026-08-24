pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t RemotePatientMonitoring .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker rm -f RemotePatientMonitoring-container || exit /b 0'
                bat 'docker run -d -p 5000:5000 --name RemotePatientMonitoring-container RemotePatientMonitoring'
            }
        }
    }

    post {
        success {
            echo 'Remote Patient Monitoring application deployed successfully!'
        }

        failure {
            echo 'Pipeline failed.'
        }
    }
}