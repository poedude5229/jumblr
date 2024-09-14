from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Blog, Post, Jote, Follow, Like

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    user = User.query.get(id)
    userdict = user.to_dict()
    blogs = Blog.query.filter(Blog.user_id == id).all()
    posts = Blog.query.filter(Post.user_id == id).all()
    userdict["blogs"] = []
    for blog in blogs:
        userdict['blogs'].append(blog.to_dict())
    userdict['posts'] = []
    for post in posts:
        userdict['posts'].append(post.to_dict())
    return jsonify(userdict)
