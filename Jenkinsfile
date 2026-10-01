pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Registration Project'
                bat 'dir'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing HTML file'
                bat 'python test.py'
            }
        }
    }

    post {

        success {
            echo 'Build and Test Successful!'
        }

        failure {
            echo 'Build or Test Failed!'
        }
    }
}