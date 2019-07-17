import os
import bcrypt
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Jamtree'
app.config["MONGO_URI"] = 'mongodb+srv://root:Welcome3@myfirstcluster-8h2g0.mongodb.net/Jamtree?retryWrites=true&w=majority'

mongo = PyMongo(app)

#CRUD

@app.route('/get_jams')
def get_jams():
    return render_template("jams.html",
    jams=mongo.db.jam_or_event.find(),
    counties=mongo.db.counties.find())

@app.route('/get_users')
def get_users():
    return render_template("users.html",
    users=mongo.db.users.find(),
    counties=mongo.db.counties.find())

@app.route('/add_jam')
def add_jam():
    return render_template('addjam.html',
    instruments=mongo.db.instruments.find(),
    counties=mongo.db.counties.find())

@app.route('/insert_jam', methods=['POST'])
def insert_jam():
    jams =  mongo.db.jam_or_event
    jams.insert_one(request.form.to_dict())
    
    print(request.form)
    return redirect(url_for('get_jams'))
    

@app.route('/delete_jam/<jam_id>')
def delete_jam(jam_id):
    mongo.db.jam_or_event.remove({'_id': ObjectId(jam_id)})
    return redirect(url_for('get_jams'))

@app.route('/edit_jam/<jam_id>')
def edit_jam(jam_id):
    the_jam =  mongo.db.jam_or_event.find_one({"_id": ObjectId(jam_id)})
    return render_template('editjam.html', jam=the_jam)

@app.route('/update_jam/<jam_id>', methods=["POST"])
def update_jam(jam_id):
    jams = mongo.db.jam_or_event
    jams.update( {'_id': ObjectId(jam_id)},
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
    return redirect(url_for('get_jams'))
    


#login system

SALT = "asdfljheriun"

@app.route('/go_to_login')
def go_to_login():
    return render_template('login.html')

@app.route('/')
def index():
    users = mongo.db.users
    if 'username' in session:
        return render_template('welcome.html')

    return render_template('jams.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    hashpw =request.form['password'] + SALT
    login_user = users.find_one({'username' : request.form['username']})

    if login_user:
        if hashpw == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return render_template('re-login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            hashpass = (request.form['password'] + SALT)
            users.insert({'username' : request.form['username'], 
            'password' : hashpass, 
            'user_county' : request.form['user_county'],
            'user_instrument' : request.form['user_instrument']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return render_template('re-register.html',
    instruments=mongo.db.instruments.find())

    return render_template('register.html',
    instruments=mongo.db.instruments.find(),
    counties=mongo.db.counties.find())

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(8080),
            debug=True)
