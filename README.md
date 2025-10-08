Docker File:
Asuuming app.py file consists of functonolity defined in the TDK Devops case study ppt.
Before testing creating docker file i will test code in my local and then in my server to ensure its working fine and then i will create docker image using docker file for contenarization.
For docker file im using the image python 3.9 slim as base image.
Assuming that app.py file is present in my current server location src directory, That's the reason i used copy command to copy src to docker container. 
If we are downloading app.py from git then we had to use add below command.
RUN git clone https://github.com/projectaws741/Ktd_L2_Test.git /app/src
Jenkisnfile:
In jenkinsfile we have multiple stages.
First stage is checkout where we will download the code from our github.
Second stage is build stage where we will build docker image.
Third stage Docker login where jenkins will login to docker based on the credentials provided in jenkins.
Fourth Stage Publishing docker Image to image artifact repo like nexus or jfrog, Here im using dockerhub for storing container images.
Fifth stage is deploying container as pod in kubernetes.
Here Assuuming jenkins and kubernetes both are running on same server.
But when comes to real world scenario we use jenkins and kubernetes servers are running in different servers. In that I will build another pipeline to deploy the pods in my kubernetes cluster by using .kubeconfig file which establishes connection between Jenkins and Kubernetes server.
K8s-cronjob.yml:
Here im using kubernetes cronkob object because this pod has to run only at 12AM ET (Assuming timings are ET). 
