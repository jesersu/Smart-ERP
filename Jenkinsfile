node {

    def buildId = currentBuild.id.padLeft(4, "0") // formateando a version 000#
    def ftpDestDir = ''
    def NOMBRESERVICIO= ''

    stage("Settings Variables") {

        if(env.BRANCH_NAME == 'desarrollo') {

            DESTDIR = "D:\\Apps\\Servicios\\MSErpProxy"
            sshIdCred = "hosting-sreasons"
            SOURCEDIR = "${env.WORKSPACE}"
            environment = "dev"
            NEXUSREPOSITORY = 'mserpproxy-dev'
            ftpDestDir = '/home/sreasons/apps/servicios/mserpproxy-dev'
            NOMBRESERVICIO = 'gunicorn-mserpproxy-dev.service'
        }
        if(env.BRANCH_NAME == 'pruebas') {

            DESTDIR = "D:\\Apps\\Servicios\\MSErpProxy"
            sshIdCred = "hosting-sreasons"
            SOURCEDIR = "${env.WORKSPACE}"
            environment = "dev"
            NEXUSREPOSITORY = 'mserpproxy-qa'
            ftpDestDir = '/home/sreasons/apps/servicios/mserpproxy-qa'
            NOMBRESERVICIO = 'gunicorn-mserpproxy-qa.service'
        }
       
    }


    stage("Git") {
        checkout scm
    }

    stage("Build") {        

    }

    stage("Release") {

        sh "rm -f dist.7z"
        sh "7z a -t7z dist.7z *"
        withCredentials([usernamePassword(credentialsId: 'nexus-credentials', passwordVariable: 'pass', usernameVariable: 'user')]) {
                sh "curl -X \"POST\" https://nexus.sreasons.com/service/rest/v1/repositories/raw/hosted   -H \"accept: application/json\"   -H \"Content-Type: application/json\"   -d \"{\\\"name\\\": \\\"${NEXUSREPOSITORY}\\\",\\\"online\\\": true,\\\"storage\\\": {\\\"blobStoreName\\\": \\\"default\\\",\\\"strictContentTypeValidation\\\": true,\\\"writePolicy\\\": \\\"ALLOW\\\"},\\\"cleanup\\\": {\\\"policyNames\\\": [\\\"string\\\"]},\\\"component\\\": {\\\"proprietaryComponents\\\": false},\\\"raw\\\": {\\\"contentDisposition\\\": \\\"ATTACHMENT\\\"}}\" --user ${user}:${pass}"
                sh "curl --user ${user}:${pass} --upload-file dist.7z https://nexus.sreasons.com/repository/${NEXUSREPOSITORY}/${NEXUSREPOSITORY}-${buildId}.7z"
        }

    }

    stage("Deploy") {
        if(env.BRANCH_NAME == 'desarrollo' || env.BRANCH_NAME == 'pruebas') {

            withCredentials([usernamePassword(credentialsId: 'nexus-credentials', passwordVariable: 'pass', usernameVariable: 'user')]) {
                script{
                    sshPublisher(
                    continueOnError: false,
                    failOnError: true,
                    publishers: [
                        sshPublisherDesc(
                        configName: sshIdCred,
                        verbose: true,
                        transfers: [
                            sshTransfer( execCommand: "sudo /bin/systemctl stop ${NOMBRESERVICIO} "),
                            sshTransfer( execCommand: "curl -o distRepo.7z -L -X GET \"https://nexus.sreasons.com/service/rest/v1/search/assets/download?sort=name&direction=desc&repository=${NEXUSREPOSITORY}\" -H \"accept: application/json\" --user ${user}:${pass} -s" ),
                            sshTransfer( execCommand: 'rm -rf '+ftpDestDir+'/* '),
                            sshTransfer( execCommand: '7z x distRepo.7z -o"' +ftpDestDir +'" '),
                            sshTransfer( execCommand: 'chmod 777 -R '+ ftpDestDir +'/*'),
                            sshTransfer( execCommand: 'rm distRepo.7z '),
                            sshTransfer( execCommand: 'chmod +x '+ ftpDestDir + '/run-on-debian.sh' ),
                            sshTransfer( execCommand: '. '+ftpDestDir+'/run-on-debian.sh ' + ' '+ NEXUSREPOSITORY),
                            sshTransfer( execCommand: "sudo /bin/systemctl start  ${NOMBRESERVICIO}")
                        ])
                    ])
                }
            }
        }
    }

}