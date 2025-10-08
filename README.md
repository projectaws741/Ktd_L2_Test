Dockerfile
	•	I am assuming the app.py file contains the functionality defined in the TDK DevOps Case Study PPT.
	•	Before creating the Dockerfile, I will first test the code locally and then on my server to ensure it works as expected. Once validated, I will create a Docker image for containerization.
	•	For the Dockerfile, I am using Python 3.9 slim as the base image.
	•	Since app.py is present in my current server’s src directory, I am using the COPY command to copy the src folder into the Docker container.
	•	If we want to download app.py (or code) directly from GitHub instead of copying it, we can use the following command in dockerfile.
RUN git clone https://github.com/projectaws741/Ktd_L2_Test.git /app/src  
Jenkinsfile

The Jenkins pipeline consists of multiple stages:
	1.	Checkout – Downloads the code from GitHub.
	2.	Build – Builds the Docker image.
	3.	Docker Login – Logs in to Docker Hub using credentials stored in Jenkins.
	4.	Publish Image – Pushes the Docker image to an artifact repository (e.g., Nexus, JFrog). In this case, Docker Hub is used for storing container images.
	5.	Deploy – Deploys the container as a pod in Kubernetes.

Here I am assuming that Jenkins and Kubernetes are running on the same server.
In real-world scenarios, Jenkins and Kubernetes typically run on different servers. In that case, I would build another pipeline for deployment that uses a .kubeconfig file to establish a secure connection between Jenkins and the Kubernetes cluster.
K8s-CronJob.yaml
	•	I am using a Kubernetes CronJob object because the container needs to run at a specific time.
	•	The CronJob is scheduled to run every day at 12 AM ET (Assuming timings are in ET)
