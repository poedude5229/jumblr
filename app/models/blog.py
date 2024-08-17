from .db import db, environment, SCHEMA, add_prefix_for_prod

class Blog(db.Model):
    __tablename__ = 'blogs'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    blog_icon_url = db.Column(db.String(255), nullable=False)
    blog_banner_url = db.Column(db.String(255))
    genre = db.Column(db.String(100), nullable=False)

    users = db.relationship("User", back_populates="blog")
    posts = db.relationship("Post", back_populates="post", cascade="all, delete-orphan")
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'blog_icon_url': self.blog_icon_url,
            'blog_banner_url': self.blog_banner_url,
            'genre': self.genre
        }
