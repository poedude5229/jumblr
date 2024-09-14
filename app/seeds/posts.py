from app.models import db, Post, environment, SCHEMA
from sqlalchemy.sql import text

def seed_posts():
    lpotl1 = Post(
        user_id=3, blog_id=1, source="Hey there, dirt people! Today we’re diving into the murky waters of Slenderman, the internet’s favorite tall, faceless boogeyman. Creepy pasta? More like scungili!", type="Text"
    )
    lpotl2 = Post(
        user_id=3, blog_id=1, source="https://jumblrbucket.s3.amazonaws.com/Episode+418_+The+Slenderman+Enigma.mp3", type="Audio"
    )
    fantasty1 = Post(
        user_id=2, blog_id=3, source="https://jumblrbucket.s3.amazonaws.com/henry-zebrowski-horse-pics-v0-bab048oiyhja1.png", type="Photo"
    )
    fantasty2 = Post(
        user_id=2, blog_id=3, source="https://jumblrbucket.s3.amazonaws.com/henry1.jpg", type="Photo"
    )
    joeblog1 = Post(
        user_id=1, blog_id=2, source="Job application is so tedious. Here's my resume, and here's all the information I put on the resume typed all over again. No, Jobot, pre-filled responses for a chat bot are not an instant interview.", type="Text"
    )
    joeblog2 = Post(
        user_id=1, blog_id=2, source="Why does my credit score go down when I pay 10 times the minimum monthly payment for my financing plan.", type="Text"
    )
    theblogofdoom1 = Post(
        user_id=4, blog_id=4, source="I don't know, I'm making this up as I go.", type="Text"
    )
    theblogofdoom2 = Post(
        user_id=4, blog_id=4, source="https://m.media-amazon.com/images/I/51utesS8hwL.jpg", type="Photo"
    )
    posts = [lpotl1, lpotl2, fantasty1, fantasty2, joeblog1, joeblog2, theblogofdoom1, theblogofdoom2]
    for post in posts:
        db.session.add(post)



    db.session.commit()

def undo_posts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.posts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
