// pipeline {
//     agent any

//     environment {
//         IMAGE_NAME = "weather_app_image"
//     }

//     stages {
//         stage('Checkout') {             
//             steps {
//                 git branch: 'mohamed_mabrouk', url: 'https://github.com/mohamedmabrouk-666/Weather-APP.git'
//      }
// }


//         stage('Build Docker Image') {
//             steps {
//                 sh 'docker build -t $IMAGE_NAME .'
//                 sh 'docker run -d -p 5000:5000 $IMAGE_NAME'
//             }
//         }
//     }

//     post {
//         success {
//             echo 'Build successful'
//         }
//         failure {
//             echo 'Build failed'
//         }
//         always {
//             echo 'Pipeline is completed'
//         }
//     }
// }
