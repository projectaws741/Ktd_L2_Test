The goal of this project was to automate a data-processing workflow for TDK:
	•	Insert raw data into an Oracle database.
	•	Fetch the same data from the database.
	•	Save it in a TSV (tab-separated) file.
	•	Schedule this process to run automatically every night at midnight.

The original app.py shared by TDK demonstrated the basic Python logic, but the task required a DevOps-ready implementation — containerized, orchestrated, and automated.

⸻

Why I We Used Docker and Docker Compose

We used Docker to package each service (Python apps and database) with its dependencies.
This ensures the application runs consistently on any system without manual setup.

Docker Compose was chosen for local orchestration because:
	•	It allows us to run multiple containers (Oracle DB, ingestion, fetch, and scheduler) together as one environment.
	•	Each container represents a distinct service but communicates seamlessly through an internal Docker network.
	•	It’s ideal for local testing before moving to Kubernetes.
	•	Configuration is simple — a single docker-compose up command brings the entire environment online.

In short, Docker Compose acts as a lightweight local cluster, simulating how services will interact later inside Kubernetes.

⸻

Why I Used Kubernetes

After validating the setup locally with Docker Compose, we used Kubernetes to deploy the same architecture in a cluster environment.

Kubernetes provides:
	•	Scalability – each microservice can scale independently based on load.
	•	Self-healing – pods are restarted automatically if they fail.
	•	Service discovery – all services communicate internally via ClusterIP networking.
	•	Persistence – the Oracle DB data is stored using a PersistentVolumeClaim (PVC).
	•	Configuration management – credentials and connection strings are stored securely as Kubernetes Secrets.

This makes the solution production-grade and cloud-ready.

⸻

Why I Created Multiple Microservices Instead of One app.py

Although TDK shared a single app.py file, it represented a monolithic design — all logic (insert, fetch, export, schedule) bundled in one process.

In DevOps and cloud-native design, we prefer microservices architecture, where each service performs one clear function and can be deployed, scaled, and maintained independently.

Benefits of this approach:
	•	Easier debugging and maintenance — one service fails, others still run.
	•	Better scalability — for example, the data fetch service can scale up without touching the scheduler.
	•	Improved CI/CD — each container can be built, tested, and deployed independently.
	•	True orchestration — aligns with the “microservices and orchestration” requirement from the TDK case study.

⸻

 End-to-End Workflow:
	1.	Scheduler triggers the pipeline every night at 00:00 AM.
	2.	Data-Ingest Service inserts fresh data into Oracle DB.
	3.	Data-Fetch Service reads data from Oracle DB and saves it to /data/output.tsv.
	4.	Oracle DB persists all records using a PersistentVolumeClaim, even after container restarts.
	5.	All services communicate internally using ClusterIP Services in Kubernetes.
