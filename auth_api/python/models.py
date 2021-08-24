from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(200))
    salt = db.Column(db.String(20))
    role = db.Column(db.String(20))

    def __repr__(self):
        return "<User %r>" % self.username
