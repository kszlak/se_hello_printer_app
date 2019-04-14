pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
                sh 'make deps'
            }
        }
        stage('Test') {
            steps {
                sh 'make test'
            }
        }
        stage('Lint') {
            steps {
                sh 'make lint'
            }
        }
        stage("testxunit") {
          steps {
            sh 'make test_xunit || true'
            xunit thresholds: [
                skipped(failureThreshold: '0'),
                failed(failureThreshold: '1')],
                tools: [
                    JUnit(deleteOutputFiles: true, failIfNotNew: true, pattern: 'test_results.xml',
                          skipNoTestFiles: false, stopProcessingIfError: true)
                ]
            }
        }
    }
}
