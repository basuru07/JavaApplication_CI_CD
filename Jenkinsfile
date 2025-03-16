pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "basuruyasaruwan/calculator"
    }
    
    stages {
        stage('SCM Checkout') {  // Clone the GitHub repository
            steps {
                retry(3) {
                    git branch: 'main', url: 'https://github.com/basuru07/pythonCalculatorPI.git'
                }
            }
        }

        stage('Build Docker Image') {  // Build the Docker image
            steps {
                script {
                    // Ensure Dockerfile exists in the repository
                    sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
                }
            }
        }

        stage('Login to Docker Hub') {  // Authenticate with Docker Hub
            steps {
                withCredentials([usernamePassword(credentialsId: 'test-dockerhubpassword', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    script {
                        sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                    }
                }
            }
        }

        stage('Push Image') {  // Push the Docker image to Docker Hub
            steps {
                script {
                    sh 'docker push ${IMAGE_NAME}:${BUILD_NUMBER}'
                }
            }
        }

        stage('Test Docker Container') {  // Run tests inside the Docker container
            steps {
                script {
                    // Pass operation and numbers as command-line arguments
                    sh 'docker run --rm ${IMAGE_NAME}:${BUILD_NUMBER} python3 calculator.py 1 10 5'
                }
            }
        }
    }

    post {
        always {
            script {
                // Clean up Docker image after the build process
                sh 'docker logout'
            }
        }
    }
}
