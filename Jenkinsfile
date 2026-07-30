sha256:2d7e26c3f9329b4c215a021319dd53cb58addd2302295b4efa5f6e10b163d090                                            application/vnd.docker.distribution.manifest.list.v2+json sha256:3e98f280fd601b37411c5fb7075fd9f337833c480f1644970b727ae0af067782 22.6 MiB  linux/amd64,linux/arm/v7,linux/arm64,linux/loong64,linux/ppc64le,linux/riscv64,linux/s390x io.cri-containerd.image=managed
sha256:305ded3f753b5dd01cd3e258cfe73510f2453d9637df6402889d25e9414cd89b                                            application/vnd.oci.image.manifest.v1+json                sha256:67b3e0f8edc483be388a1813ed215af912db9ea65f8cfe6c0182a8ab47ed538d 130.4 MiB linux/amd64                                                                                io.cri-containerd.image=managed
sha256:6270bb605e12e581514ada5fd5b3216f727db55dc87d5889c790e4c760683fee                                            application/vnd.docker.distribution.manifest.list.v2+json sha256:74c4244427b7312c5b901fe0f67cbc53683d06f4f24c6faee65d4182bf0fa893 294.4 KiB linux/amd64,linux/arm/v7,linux/arm64,linux/s390x,windows/amd64                             io.cri-containerd.image=managed
sha256:9254fb81aa65831cce153dfdf883805d40157b78ccec0c10fd82c499113fd1de                                            application/vnd.oci.image.index.v1+json                   sha256:1eba82e9c386038b4af6d69cca7519fac738c28c42735ed48ce70c882ad0d80f 85.2 MiB  linux/amd64,linux/arm/v7,linux/arm64,linux/ppc64le,linux/riscv64,linux/s390x               io.cri-containerd.image=managed
sha256:e0e34c2c9f8ab01e31b463de1d40cdd12d9dd1691900213adedf776deac7bce5                                            application/vnd.oci.image.index.v1+json                   sha256:939b8f2fbb793483a8716464f8c7de9726dfb50393ad02b99b652004b5503ee6 60.8 MiB  linux/amd64,linux/arm/v7,linux/arm64                                                       io.cri-containerd.image=managed
sha256:e76b3f3568b7f440dfd477c1d6de638d7769ba34c93eef999dee418eb72bc0e3                                            application/vnd.docker.distribution.manifest.list.v2+json sha256:b2d2efaf5ac3b366ed0f839d2412a2c4279d4fc2a2a733f12c52133faed36c41 21.5 MiB  linux/amd64,linux/arm/v7,linux/arm64/v8,linux/ppc64le,linux/s390x                          io.cri-containerd.image=managed
sha256:eaa1212a2b4569c811bfa0ad5708428703ad3120a6dbae3b4353ec3cb36f36d2                                            application/vnd.oci.image.index.v1+json                   sha256:910944bb0bd94f060a82a56ca1ea1c577d3e49b3473a093a47a985f32e92d94a 5.0 MiB   linux/amd64,linux/arm/v7,linux/arm64                                                       io.cri-containerd.image=managed
sha256:f66893ac132535099f7ef6c40ca1636f6a89f2c373c0eef28dd84537928ec0b6                                            application/vnd.oci.image.index.v1+json                   sha256:fcdef599e6259359833dd2e1d49f9e964f66825d69bd3dd468f51102ce013d03 50.6 MiB  linux/amd64,linux/arm/v6,linux/arm64/v8,linux/ppc64le,linux/riscv64,linux/s390x            io.cri-containerd.image=managed
[root@ip-172-31-1-200 employee-app]# vi Jenkinsfile

        stage('Export Docker Image') {
            steps {
                sh '''
                docker save ${IMAGE_NAME} -o k8s/employee-app.tar
                '''
            }
        }

        stage('Import Image into K3s') {
            steps {
                sh '''
                sudo k3s ctr images import k8s/employee-app.tar
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/namespace.yaml
                kubectl apply -f k8s/deployment.yaml
                kubectl apply -f k8s/service.yaml

                kubectl rollout restart deployment employee-app -n employee
                kubectl rollout status deployment employee-app -n employee
                '''
            }
        }
    }

    post {
        success {
            echo "Deployment completed successfully!"
        }

        failure {
            echo "Deployment failed!"
        }
    }
}

