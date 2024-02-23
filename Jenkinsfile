pipeline {
    agent {
        node {
            label 'docker-agent-python'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building Stage.."
                sh '''
                pwd
                ls -al
                cd myapp
                pwd
                pip install -r requirements.txt
                echo "doing build stuff.."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing Stage.."
                sh '''
                cd myapp
                pwd
                python3 hello.py
                python3 hello.py --name=mmi
                python3 hello.py --name=mmi > mmi.txt
                echo "doing test stuff.."
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Delivering Stage....'
                sh '''
                cd myapp
                pwd
                ls -la
                cat mmi.txt
                lscpu
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
