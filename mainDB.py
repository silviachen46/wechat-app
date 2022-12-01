from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from pip import main
import time
import pandas as pd
# app=Flask(__name__)


db = SQLAlchemy()

def initDB(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'data.db'
    #os.path.join(app.root_path, 'data.db')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app)

#initDB(app)

class MenuModel(db.Model):
    __tablename__="Menu"
    menu_id=db.Column(db.Integer,primary_key=True)#主键自动递增
    menuname=db.Column(db.String(64),nullable=True)
    foodused=db.Column(db.String(64),nullable=True)
    taste=db.Column(db.String(64),nullable=True)
    cook_method=db.Column(db.String(64),nullable=True)
    region=db.Column(db.String(64),nullable=True)
    url=db.Column(db.String(64),nullable=True)
   
class FoodModel(db.Model):
    __tablename__='Foods'
    food_id=db.Column(db.Integer,primary_key=True)
    foodname = db.Column(db.String(64),nullable=False)
    date_till=db.Column(db.String(64),nullable=True)
    mass=db.Column(db.String(64),nullable=True)
    #stuid=db.Column(db.Integer,db.ForeignKey('students.id'))
    #courid=db.Column(db.Integer,db.ForeignKey('course.id'))


if __name__=='__main__':
    db.create_all()
    #db.drop_all()