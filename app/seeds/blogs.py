from app.models import db, Blog, environment, SCHEMA
from sqlalchemy.sql import text

def seed_blogs():
    lpotl = Blog(
        user_id=3, name="The Last Blog on the Left", blog_icon_url="https://jumblrbucket.s3.amazonaws.com/lpotl_10.10.22.jpg", genre="Comedy"
    )

    db.session.add(lpotl)
    db.session.commit()

def undo_blogs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.blogs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM blogs"))

    db.session.commit()
