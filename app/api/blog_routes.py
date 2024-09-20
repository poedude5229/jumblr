from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User, Blog, Post, Jote, Follow, Like

blog_routes = Blueprint('blogs', __name__)

@blog_routes.route('/')
def blogs():
    blogs = Blog.query.all()
    return {'blogs': [blog.to_dict() for blog in blogs]}

@blog_routes.route('/<type>')
def blogs_by_type(type):
    blogs2 = Blog.query.filter(Blog.genre == type)
    return {'blogs': [blog.to_dict() for blog in blogs2]}
