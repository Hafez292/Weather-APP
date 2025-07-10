pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ziadkh/weather_app:v1'
        DOCKER_CREDENTIALS_ID = '367eb5fa-29a0-40a5-ae8e-47eb5cb6cda4'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/Ziad-kh99/Weather-APP.git', branch: 'app_v1'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${IMAGE_NAME}").push()
                    }
                }
            }
        }
    }
}