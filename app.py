import os
from flask import Flask, request, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

MONGO_URI = os.environ['MONGO_URI']
app.config["MONGO_URI"] = MONGO_URI 
app.config["MONGO_DBNAME"] = 'workout_tracker'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_workouts')
def get_workouts():
    return render_template('workouts.html', workouts=mongo.db.workouts.find())

@app.route('/add_workout')
def add_workout():
        return render_template('addworkout.html', 
        categories=mongo.db.MuscleCategory.find())

@app.route('/insert_workout', methods=['POST'])
def insert_workout():
    workouts = mongo.db.workouts
    workouts.insert_one(request.form.to_dict())
    return redirect(url_for('get_workouts'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)