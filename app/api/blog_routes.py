from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Blog, Post, Jote, Follow, Like
from .aws_helpers import upload_file_to_s3, get_unique_filename


blog_routes = Blueprint('blogs', __name__)

@blog_routes.route('/', methods=["GET"])
def blogs():
    blogs = Blog.query.all()
    return {'blogs': [blog.to_dict() for blog in blogs]}

# @blog_routes.route('/user_blogs/<user>')
# def blogs_by_user(user):
#     specified_blogowner = User.query.filter(User.username == user).all()           ##Work on this shit later
#     blogs3 = Blog.query.filter(Blog.user_id == specified_blogowner.id).all()
#     return {'user_blogs': [blog.to_dict() for blog in blogs3]}

# @blog_routes.route("/new", methods=["POST"])
# @login_required                              #Do after blog form
# def new_blog():
#     return

@blog_routes.route('/<type>', methods=["GET"])
def blogs_by_type(type):
    blogs2 = Blog.query.filter(Blog.genre == type).all()
    return {'blogs': [blog.to_dict() for blog in blogs2]}

@blog_routes.route('/<int:id>', methods=["GET"])
def blog_by_id(id):
    blog3 = Blog.query.get(id)
    return {'blog': blog3.to_dict()}

@blog_routes.route('/search/<string:substring>', methods=["GET"])
def blog_by_string(substring):
    blogs3 = Blog.query.filter(Blog.name.ilike(f"%{substring}%")).all()
    return {'blogs': [blog.to_dict() for blog in blogs3]}

@blog_routes.route('/users/<string:username>', methods=["GET"])
def blog_by_owner_username(username):
    owner = User.query.filter(User.username.ilike(f"%{username}%")).first()

    if not owner:
        return {'message': 'User not found'}, 404
    blogs4 = Blog.query.filter(Blog.user_id == owner.id).all()

    return {'blogs': [blog.to_dict() for blog in blogs4]}
