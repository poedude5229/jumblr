from .db import db, environment, SCHEMA, add_prefix_for_prod

class Jote(db.Model):
    __tablename__ = 'jotes'

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}
