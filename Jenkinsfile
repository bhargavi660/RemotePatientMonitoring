pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t RemotePatientMonitoring .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f RemotePatientMonitoring-container || true'
                sh 'docker run -d -p 5000:5000 --name RemotePatientMonitoring-container RemotePatientMonitoring'
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