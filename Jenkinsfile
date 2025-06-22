@Library("Shared") _

pipeline{
    
    agent { label "vinod" }
    stages{
        stage("Code"){
            steps{
                clone("https://github.com/Vardaan-02/basic-python-server.git","main")
            }
        }
        stage("Build") {
            steps {
                script {
                    docker_build("flask-app","latest","vardaan02")
                }
            }
        }
        stage("Dokcer-Hub"){
            steps{
                script{
                    docker_push("flask-app","latest","docker-hub")
                }
            }
        }
        stage("Deploy"){
            steps{
                echo "Deploying"
                sh "docker compose down && docker compose up -d"
            }
        }
    }
}