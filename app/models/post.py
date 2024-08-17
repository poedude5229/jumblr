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

    users = db.relationship("User", back_populates="post")
    blogs = db.relationship("Blog", back_populates="post")
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'blog_id': self.blog_id,
            'source': self.source,
            'type': self.type
        }
