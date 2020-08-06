from . import db
# from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy import  ForeignKey


blogs_and_tags = db.Table("blogs and tags", db.Column("blog_id", db.Integer, ForeignKey('blog.id')),
                          db.Column("tag_id", db.Integer, ForeignKey('tags.id')))

class User(db.Model):
    __tablename__ = "user"
    email = db.Column(db.String(64), primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    blog = relationship("Blog", back_populates="user")


class Blog(db.Model):
    __tablename__ = "blog"
    id = db.Column(db.Integer, primary_key=True)
    blog = db.Column(db.String)
    blog_headline = db.Column(db.String(100))
    user_email = db.Column(db.String(64), ForeignKey('user.email'))
    publising_date = db.Column(db.Date)
    user = relationship("User", back_populates="blog")
    tags = relationship("Tags", secondary=blogs_and_tags)


class Tags(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(30), unique=True)
    blogs = relationship("Blog", secondary=blogs_and_tags)
