from app.models import db, Blog, environment, SCHEMA
from sqlalchemy.sql import text

def seed_blogs():
    lpotl = Blog(
        user_id=3, name="The Last Blog on the Left", blog_icon_url="https://jumblrbucket.s3.amazonaws.com/lpotl_10.10.22.jpg", genre="Comedy"
    )
    joeblog = Blog(
        user_id=1, name="The Joe Blawg", blog_icon_url="https://avatars.githubusercontent.com/u/148486236?v=4", blog_banner_url="https://bandfishbucket.s3.amazonaws.com/NRG95Bridge95startrails95FINAL.JPG", genre="Personal"
    )
    fantastyblog = Blog(
        user_id=2, name="Henry Zebrowski Horse Pic Emporium", blog_icon_url="https://preview.redd.it/henry-zebrowski-horse-pics-v0-bab048oiyhja1.jpeg?width=2603&format=pjpg&auto=webp&s=72025fef4cd850c5cfee0c55c3f1fc1fca3cff4f", blog_banner_url="https://www.tvguide.com/a/img/resize/2613849ce2c63ce4054d42345e5797f3eeeb4eb1/catalog/provider/1/6/1-511802708.jpg?auto=webp&fit=crop&height=675&width=1200", genre="Comedy"
    )
    theblogofdoom = Blog(
        user_id=4, name="The Blog Of Doom", blog_icon_url="https://assets-prd.ignimgs.com/2023/04/03/img-5044-1680550489953.jpg?width=3840", blog_banner_url="https://static.wikia.nocookie.net/indianajones/images/9/97/Templeofdoom.jpg/revision/latest?cb=20180909195402", genre="Travel"
    )

    db.session.add(lpotl)
    db.session.add(joeblog)
    db.session.add(fantastyblog)
    db.session.add(theblogofdoom)
    db.session.commit()

def undo_blogs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.blogs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM blogs"))

    db.session.commit()
