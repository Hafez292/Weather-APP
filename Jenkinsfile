pipeline {
    agent any

    environment {
        IMAGE_NAME = 'ziadkh/weather_app:v1'
        DOCKER_CREDENTIALS_ID = 'dockerhub'
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
                    def credsId = env.DOCKER_CREDENTIALS_ID.toString()
                    docker.withRegistry('https://index.docker.io/v1/', credsId) {
                        docker.image("${IMAGE_NAME}").push()
                    }
                }
            }
        }
    }
}