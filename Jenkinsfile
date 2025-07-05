pipeline {
    agent any

    environment {
        IMAGE_NAME = "/home/mohamed/project/weather_project/my_vevn"
       
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/username/weather_project.git' // غيّر الرابط حسب مشروعك
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
                sh 'docker run -p 5000:5000 weather_project'

            }
        }


    }

     post {

        success
        {
              echo 'successful'
        }

        faliyre
        {
             echo 'failed'

        }
        always 
        {
            echo 'pipline is competed'
            
        }
    }

}

