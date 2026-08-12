
// webhook test
pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\User\\AppData\\Local\\Python\\bin\\python.exe -m pip install -r requirements.txt'
                bat 'C:\\Users\\User\\AppData\\Local\\Python\\bin\\python.exe -m playwright install chromium'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\User\\AppData\\Local\\Python\\bin\\python.exe -m pytest'
            }
        }
    }
}