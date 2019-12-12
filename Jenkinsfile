pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Started Build'
        echo '...'
        echo 'Build Successful'
      }
    }
    stage('Test') {
      steps {
        echo 'Started Testing'
        echo '...'
        echo 'Test Successfull'
      }
    }
  }
  environment {
    PGHOST = 'postgres'
  }
}