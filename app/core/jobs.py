# app/core/jobs.py
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .vies import recheck_due_batches, persist_results, email_report

def setup_scheduler():
    sch = AsyncIOScheduler()
    sch.add_job(recheck_due_batches, "cron", day="1", hour=2)  # mtl. Re-Check
    sch.start()
