from app.models import db, Follow, environment, SCHEMA
from sqlalchemy.sql import text

def seed_follows():
    follow1 = Follow(
        followed_user_id=3, follower_id=1
    )
    db.session.add(follow1)
    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUCATE table {SCHEMA}.follows RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM follows"))
    db.session.commit()
