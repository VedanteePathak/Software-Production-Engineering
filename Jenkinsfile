pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE_NAME = 'calcpython'
        GITHUB_REPO_URL = 'https://github.com/VedanteePathak/Software-Production-Engineering.git'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the GitHub repository
                git branch: 'main', url: "${GITHUB_REPO_URL}"
            }
        }
        
        stage('Build the Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }
            }
        }
        
        stage('Push the Docker Image') {
            steps {
                script{
                    docker.withRegistry('', 'docker_hub') {
                    sh 'docker tag "${DOCKER_IMAGE_NAME}" vedanteepathak/calcpython:latest'
                    sh 'docker push vedanteepathak/calcpython'
                    }
                 }
            }
        }
        
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }
    }
}
