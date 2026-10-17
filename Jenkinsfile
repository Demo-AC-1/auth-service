pipeline {
  agent any
  environment { IMAGE = 'registry.acme.example/identity/auth-service' }
  stages {
    stage('Build') { steps { sh 'docker build -t $IMAGE:$BUILD_NUMBER .' } }
    stage('Push')  { steps { sh 'docker push $IMAGE:$BUILD_NUMBER' } }
    stage('Deploy') { steps { sh 'kubectl set image deployment/auth-service app=$IMAGE:$BUILD_NUMBER' } }
  }
}
