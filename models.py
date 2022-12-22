"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/checkmark-png-28.png"


class User(db.Model):
    """user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    post = db.relationship('Post')

    @property
    def full_name(self):
        """Return name of user."""

        return f"{self.first_name} {self.last_name}"


def connect_db(app):
 

    db.app = app
    db.init_app(app)


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    title = db.Column(db.String(40), nullable = False, unique = True)
    content = db.Column(db.Text, nullable = False, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User')
