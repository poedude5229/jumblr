from .db import db, environment, SCHEMA, add_prefix_for_prod

class Jote(db.Model):
    __tablename__ = 'jotes'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    body = db.Column(db.String(255))

    user = db.relationship("User", back_populates="jote")
    post = db.relationship("Post", back_populates="jote")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'body': self.body
        }
