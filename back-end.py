from flask import Flask
import time
from flask_sqlalchemy import SQLAlchemy
import logging
import json
from mainDB import db,MenuModel,FoodModel, initDB
from flask import request, send_from_directory, jsonify
from sqlalchemy import or_,and_
from datetime import datetime,timedelta,timezone


app = Flask(__name__)
initDB(app)

app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8" #指定浏览器渲染的文件类型，和解码格式；

class Menu:
    menu_id = 0
    menuname = ''
    foodused = ''
    taste= ''
    cook_method= ''
    region=''
    url = ''

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4,ensure_ascii=False)

class Food:
    food_id = 0
    food_name = 'test'
    date_till= 0
    mass= 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4,ensure_ascii=False)



@app.route('/food', methods=['GET'])
def get_all_food():
    return_value=""
    food_models=FoodModel.query.all()
    
    foods=[]
        
    for food_model in food_models:
        food = Food()
        food.food_id = food_model.food_id
        food.food_name = food_model.foodname
        #print(food.food_name)
        food.date_till = food_model.date_till
        food.mass = food_model.mass  
        foods.append(food)
        if return_value!="":
                return_value += ','
        return_value += food.toJSON()
    return_value = '[' + return_value + ']'
    return return_value
    # return jsonify([
    #   {"food_id": 1, "food_name": 'test1'},
    #   {"food_id": 2, "food_name": 'test2'}
    # ])


@app.route('/food', methods=['DELETE'])
def Delete():
    food_models=FoodModel.query.all()
    for food_model in food_models:
        db.session.delete(food_model)
    db.session.commit()
    val="暂无数据！"
    db.session.close()
    return val

@app.route('/menu', methods=['GET'])
def menu_search():
    query = request.args.get('query')
    
    # menuFilter={or_(MenuModel.region == query,
    #                 MenuModel.menuname == query,
    #                 MenuModel.taste==query,
    #                 MenuModel.cook_method==query,
    #                 MenuModel.menuname.contains("%s")%query  MenuModel.menuname.like("%/%s%")%query
    #                                 )}
    # Retrieve food data according to food_id MenuModel.menuname.like("%/%s%")%query
    return_value = ''
    food_models=FoodModel.query.all()
    menu_dbs = MenuModel.query.filter(or_(MenuModel.region == query,
                    MenuModel.menuname == query,
                    MenuModel.taste==query,
                    MenuModel.cook_method==query,
                    #MenuModel.menuname.contains("%s")%query  
                    MenuModel.menuname.like('%'+query+'%'),
                    MenuModel.foodused == query
                                    )).all()
      
   
    for menu_db in menu_dbs:
         for food_m in food_models:    
            if food_m.foodname in menu_db.foodused:

                menu = Menu()
                menu.menu_id = menu_db.menu_id
                menu.menuname = menu_db.menuname
                menu.foodused = menu_db.foodused
                menu.taste = menu_db.taste
                menu.cook_method = menu_db.cook_method
                menu.region =menu_db.region
                menu.url = menu_db.url
        
                if return_value!="":
                    return_value += ','
                return_value += menu.toJSON()
    
    return_value = '[' + return_value + ']'
    
    return return_value
    



@app.route('/food', methods=['POST'])
def create_food():
    foodInput = request.json#request含有提交的数据
    print(foodInput)
    food_name = foodInput['food_name']
    date_till = foodInput['date_till']
    mass=foodInput['mass']

    f = FoodModel(
            foodname=food_name,
            date_till=date_till,
            mass=mass,
        )
    db.session.add(f)
    db.session.commit()
    
    return jsonify({'success': True})
    
    
    #foodInput = request.json#request含有提交的数据
    
    # Set values of the food with the input from API
    
    # Save the food object into DB.
    


@app.route('/food', methods=['PUT'])
def update_food():
    food_id = request.args.get('foodId')
    foodInput = request.json
    # Retrive food from DB
    food = Food()
    food.food_id = food_id
    # Update retrieved food with the input from API
    food.food_name = foodInput['food_name']
    return food.toJSON()


app.run(host='127.0.0.1',port=5000,debug=True)