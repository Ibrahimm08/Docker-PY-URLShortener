from .models import Url
from app import db
from datetime import datetime, date
from sqlalchemy import func
from apscheduler.schedulers.background import BackgroundScheduler

today = datetime.today()

# Get and delete rows that meet the expiry date
def delete_expired_rows():
    db.session.query(Url).filter(func.date(Url.expires_at) <= today).delete()
    db.session.commit()

scheduler = BackgroundScheduler()

# Run function at 2 hour intervals
def start_scheduler():
    scheduler.add_job(delete_expired_rows, "interval", hours=2)
    scheduler.start()
