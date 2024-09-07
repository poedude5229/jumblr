from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text

def seed_posts():
    lpotl1 = Post(
        user_id=3, blog_id=1, source="Hey there, dirt people! Today we’re diving into the murky waters of Slenderman, the internet’s favorite tall, faceless boogeyman. Creepy pasta? More like scungili!", type="Text"
    )
    lpotl2 = Post(
        user_id=3, blog_id=1, source="https://jumblrbucket.s3.amazonaws.com/Episode+418_+The+Slenderman+Enigma.mp3", type="Audio"
    )
    posts = [lpotl1, lpotl2]
    for post in posts:
        db.session.add(post)



    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
