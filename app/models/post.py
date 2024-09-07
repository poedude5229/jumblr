from .db import db, environment, SCHEMA, add_prefix_for_prod

class Post(db.Model):
    __tablename__ = 'posts'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'), nullable=False)
    source = db.Column(db.String(255))
    type = db.Column(db.String(50))

    user = db.relationship("User", back_populates="post")
    blog = db.relationship("Blog", back_populates="post")
    jote = db.relationship("Jote", back_populates="post", cascade="all, delete-orphan")
    like = db.relationship("Like", back_populates="post", cascade="all, delete-orphan")
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'blog_id': self.blog_id,
            'source': self.source,
            'type': self.type
        }
