from .db import db, environment, SCHEMA, add_prefix_for_prod

class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
