from .db import db, environment, SCHEMA, add_prefix_for_prod

class Blog(db.Model):
    __tablename__ = 'blogs'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
