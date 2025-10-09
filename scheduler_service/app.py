from apscheduler.schedulers.blocking import BlockingScheduler
import requests, time

scheduler = BlockingScheduler()

def run_pipeline():
    try:
        print("Running nightly pipeline...")
        requests.post("http://data_ingest_service:5000/ingest", json={"name": "TDK", "value": 100})
        requests.get("http://data_fetch_service:5000/fetch")
        print("Pipeline run completed successfully.")
    except Exception as e:
        print(f"Pipeline failed: {e}")

scheduler.add_job(run_pipeline, 'cron', hour=0, minute=0)

if __name__ == '__main__':
    print("Scheduler service started. Waiting for midnight job...")
    time.sleep(60)  # allow other services to initialize
    run_pipeline()  # optional: trigger once on startup
    scheduler.start()
