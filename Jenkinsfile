pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t remotepatientmonitoring .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker rm -f remotepatientmonitoring-container || true
                    docker run -d -p 5000:5000 --name remotepatientmonitoring-container remotepatientmonitoring
                '''
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