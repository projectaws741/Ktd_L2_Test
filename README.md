Workflow:
	1.	Data-Ingest Service → Inserts raw data into Oracle DB.
	2.	Data-Fetch Service → Fetches data from DB and saves it to output.tsv.
	3.	Scheduler Service → Triggers the pipeline automatically at 00:00 AM daily.
	4.	Oracle DB → Stores the persistent data.

Run Locally with Docker Compose:

Prerequisites

Before you start, ensure you have installed:
	•	Docker Desktop
	•	Docker Compose
Folder Structure:
Ktd_L2_Test/
│
├── docker-compose.yml
├── .env
├── data/
│   └── output.tsv (auto-created)
│
├── data_ingest_service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── data_fetch_service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── scheduler_service/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
Environment Variables

All configuration parameters are managed through the .env file.

Example .env:
# Oracle DB Configuration
ORACLE_USER=system
ORACLE_PASSWORD=oracle
ORACLE_DSN=oracle-db/XEPDB1

# Export Path
DATA_PATH=/data/output.tsv

Steps to Run Locally:
Step 1: Clone the Repository
#git clone https://github.com/projectaws741/Ktd_L2_Test.git
#cd Ktd_L2_Test

Step 2: Start the Containers
#docker-compose up -d
This command will:
	•	Pull and start Oracle XE DB.
	•	Build and run three microservices (ingest, fetch, scheduler).
	•	Create a shared volume for persistent Oracle data.
	•	Map local folder ./data for storing TSV output.

Step 3: Verify Running Containers
#docker ps
You should see containers:
oracle-db
data_ingest_service
data_fetch_service
scheduler_service
#docker container ls
You should see the containers below.
<img width="1280" height="186" alt="image" src="https://github.com/user-attachments/assets/fe419719-9761-4c62-bd07-fdf26ed88d9b" />
Step 4: Test the Services Manually
Insert Data:
#curl -X POST http://localhost:5001/ingest \
     -H "Content-Type: application/json" \
     -d '{"name":"TDK","value":100}'
Fetch and Export Data:
#curl http://localhost:5002/fetch
Check if file was created:
#cat data/output.tsv
Verify Automatic Scheduler:
The scheduler service runs daily at 00:00 AM local time.
You can check logs to confirm:
#docker logs scheduler_service

Clean Up:
#docker-compose down
To remove all images and volumes (start clean):
#docker-compose down -v

Moving to Kubernetes:

The same architecture can be deployed to Kubernetes using manifests in the kubernetes/ folder.

Each service has:
	•	Deployment – manages pods and replicas
	•	Service (ClusterIP) – allows internal communication
	•	Secret – stores credentials securely
	•	PVC – provides persistent Oracle storage
To deploy:
#kubectl apply -f kubernetes/


