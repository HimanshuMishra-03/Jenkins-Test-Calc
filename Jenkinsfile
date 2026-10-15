pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    def projectDir = fileExists('JenkinsPractical-9/requirements.txt')
                        ? 'JenkinsPractical-9'
                        : '.'
                    if (isUnix()) {
                        sh "python3 -m pip install -r '${projectDir}/requirements.txt'"
                    } else {
                        bat "python -m pip install -r ${projectDir}/requirements.txt"
                    }
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    def projectDir = fileExists('JenkinsPractical-9/test_calculator.py')
                        ? 'JenkinsPractical-9'
                        : '.'
                    if (isUnix()) {
                        sh "python3 -m pytest -v '${projectDir}/test_calculator.py' --junitxml='${projectDir}/test-results.xml'"
                    } else {
                        bat "python -m pytest -v ${projectDir}/test_calculator.py --junitxml=${projectDir}/test-results.xml"
                    }
                }
            }
        }
    }

    post {
        always {
            junit testResults: '**/test-results.xml', allowEmptyResults: true
        }
    }
}
