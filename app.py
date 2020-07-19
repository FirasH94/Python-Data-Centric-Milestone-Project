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

@app.route('/edit_workout/<workout_id>')
def edit_workout(workout_id):
    my_workout = mongo.db.workouts.find_one({"_id" : ObjectId(workout_id)})
    all_categories = mongo.db.MuscleCategory.find()
    return render_template('editworkout.html', workout=my_workout, categories=all_categories)

@app.route('/update_workout/<workout_id>', methods=["POST"])
def update_workout(workout_id):
    workouts = mongo.db.workouts
    workouts.update( {'_id': ObjectId(workout_id)},
    {
        'workout_name':request.form.get('workout_name'),
        'muscle_name':request.form.get('muscle_name'),
        'workout_notes': request.form.get('workout_notes'),
        'sets': request.form.get('sets'),
        'reps': request.form.get('reps'),
        'pr_weight': request.form.get('pr_weight'),
        'workout_date': request.form.get('workout_date')
    })
    return redirect(url_for('get_workouts'))

@app.route('/delete_workout/<workout_id>')
def delete_workout(workout_id):
    mongo.db.workouts.remove({'_id': ObjectId(workout_id)})
    return redirect(url_for('get_workouts'))

@app.route('/get_categories')
def get_categories():
    return render_template('categories.html', categories=mongo.db.MuscleCategory.find())

@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.MuscleCategory.find_one(
                           {'_id': ObjectId(category_id)}))

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.MuscleCategory.update(
        {'_id': ObjectId(category_id)},
        {'muscle_name': request.form.get('muscle_name')})
    return redirect(url_for('get_categories'))

@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.MuscleCategory.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))

@app.route('/insert_category', methods=['POST'])
def insert_category():
    category_doc = {'muscle_name': request.form.get('muscle_name')}
    mongo.db.MuscleCategory.insert_one(category_doc)
    return redirect(url_for('get_categories'))

@app.route('/add_category')
def add_category():
    return render_template('addcategory.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)