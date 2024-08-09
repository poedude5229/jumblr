from .db import db, environment, SCHEMA, add_prefix_for_prod

class Follow(db.Model):
    __tablename__ = 'follows'

    if environment == 'production':
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    followed_user_id = db.Column(db.Integer)
    follower_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'followed_user_id': self.followed_user_id,
            'follower_id': self.follower_id
        }
