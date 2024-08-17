from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    joe = User(
        username='Joe420', email='skinnyjoe@joerashid.xyz', password='espookyspaghetti333', bio="I created you")
    henry = User(
        username='HBONE', email='hzebrowski@sidestories.lpotl', password='password', bio="The best comedian both sides of the Mississipp'")
    ben = User(
        username='kisseldawg', email='grant@kissel.ben', password='password', bio="LPOTL is less funny without me")

    db.session.add(joe)
    db.session.add(henry)
    db.session.add(ben)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
