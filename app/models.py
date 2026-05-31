from app import db

# Deffines database table called url
class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_code = db.Column(db.String(10), unique=True, nullable=False)
    long_url = db.Column(db.String(2048), nullable=False)
    page_title = db.Column(db.String(2048), nullable = False)
    expires_at = db.Column(db.Date, nullable = True)
