pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        DOCKERHUB_REPO = 'pintop9'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/pintop9/flask-contacts.git'
            }
        }

        stage('Test Docker Login') {
            steps {
                script {
                    sh '''
                    echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin
                    '''
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    try {
                        // Check the paths to Dockerfiles and adjust if necessary
                        docker.build("${DOCKERHUB_REPO}/contacts-web", "-f Dockerfile .")
                        docker.build("${DOCKERHUB_REPO}/contacts-db", "-f ./Docker/db/Dockerfile .")
                    } catch (Exception e) {
                        echo "Failed to build Docker images: ${e}"
                        throw e
                    }
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials-id') {
                        docker.image("${env.DOCKERHUB_REPO}/contacts-web").push('latest')
                        docker.image("${env.DOCKERHUB_REPO}/contacts-db").push('latest')
                    }
                }
            }
        }

        stage('Run Docker Containers') {
            steps {
        sh '''
            docker rm -f contacts-web contacts-db || true
            docker run -d --name contacts-db --restart unless-stopped -e POSTGRES_DB=contacts_db -e POSTGRES_USER=contacts_user -e POSTGRES_PASSWORD=contacts_pass ${DOCKERHUB_REPO}/contacts-db
            sleep 20
            docker run -d --name contacts-web --link contacts-db:db -p 5000:5000 --restart unless-stopped ${DOCKERHUB_REPO}/contacts-web
        '''
        sh '''
            docker exec contacts-db psql -U contacts_user -d contacts_db -c "DROP TABLE IF EXISTS contacts;"
        '''
        // Run database migrations
        sh '''
            docker exec contacts-web sh -c "export FLASK_APP=app.py && flask db init"
            docker exec contacts-web sh -c "flask db migrate && flask db upgrade"
            docker exec contacts-web sh -c "export FLASK_APP=app.py && python migrations.py"
        '''
            }
        }
    }
}
