import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Jamtree'
app.config["MONGO_URI"] = 'mongodb+srv://root:Welcome3@myfirstcluster-8h2g0.mongodb.net/Jamtree?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_jams')
def get_jams():
    return render_template("jams.html", jams=mongo.db.jam_or_event.find())

@app.route('/add_jam')
def add_jam():
    return render_template('addjam.html')

@app.route('/insert_jam', methods=['POST'])
def insert_jam():
    jams =  mongo.db.jam_or_event
    jams.insert_one(request.form.to_dict())
    return redirect(url_for('get_jams'))

@app.route('/delete_jam/<jam_id>')
def delete_jam(jam_id):
    mongo.db.jam_or_event.remove({'_id': ObjectId(jam_id)})
    return redirect(url_for('get_jams'))

@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    the_task =  mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edittask.html', task=the_task,
                           categories=all_categories)

@app.route('/update_jam/<jam_id>', methods=["POST"])
def update_jam(jam_id):
    jams = mongo.db.jam_or_event
    jam_or_event.update( {'_id': ObjectId(jam_id)},
    {
        'jam_title':request.form.get('jam_title'),
        'genre':request.form.get('genre'),
        'date_of_jam': request.form.get('date_of_jam'),
        'jam_location': request.form.get('jam_location'),
        'jam_postcode':request.form.get('jam_postcode'),
        'jam_members':request.form.get('jam_members'),
        'jam_instruments':request.form.get('jam_instruments'),
        'jam_notes':request.form.get('jam_notes'),
    })
    return redirect(url_for('get_tasks'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)