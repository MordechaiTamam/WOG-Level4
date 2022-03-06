pipeline {
    agent { label 'agent_1' }
    stages {
        stage('Build docker image'){
            steps{
                sh 'docker build -t moditamam/selenium:from-jenkins-pipeline .'
            }
        }
        stage('list files') {
            agent {
                docker {
                    image "moditamam/selenium:from-jenkins-pipeline"
                    reuseNode true
                }
            }
            steps {
                sh 'python3 /app/MainScores.py'
                sh 'sleep 5'
                sh 'python3 e2e.py'
            }
        }
    }
}