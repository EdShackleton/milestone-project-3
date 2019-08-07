import os
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
    user_logged_in = 'username' in session
    if user_logged_in:
        return render_template("jams.html",
        jams=mongo.db.jam_or_event.find(),
        counties=mongo.db.counties.find(),
        username=session['username'],
        user_logged_in=user_logged_in)
    return render_template("jams.html",
    jams=mongo.db.jam_or_event.find(),
    counties=mongo.db.counties.find(),
    user_logged_in=user_logged_in)

@app.route('/get_users')
def get_users():
    user_logged_in = 'username' in session
    if user_logged_in:
        return render_template("users.html",
        users=mongo.db.users.find(),
        counties=mongo.db.counties.find(),
        username=session['username'],
        user_logged_in=user_logged_in)
    return render_template("users.html",
        users=mongo.db.users.find(),
        counties=mongo.db.counties.find(),
        user_logged_in=user_logged_in)

@app.route('/add_jam', methods=['POST', 'GET'])
def add_jam():
    user_logged_in = 'username' in session
    if request.method == 'POST':
        jams =  mongo.db.jam_or_event
        jams.insert_one({
                'jam_title':request.form.get('jam_title'),
                'genre':request.form.get('genre'),
                'date_of_jam': request.form.get('date_of_jam'),
                'jam_location': request.form.get('jam_location'),
                'jam_county':request.form.get('jam_county'),
                'jam_member_1':request.form.get('jam_member_1'),
                'jam_member_2':request.form.get('jam_member_2'),
                'jam_member_3':request.form.get('jam_member_3'),
                'jam_member_4':request.form.get('jam_member_4'),
                'jam_member_5':request.form.get('jam_member_5'),
                'jam_member_6':request.form.get('jam_member_6'),
                'jam_member_7':request.form.get('jam_member_7'),
                'jam_member_8':request.form.get('jam_member_8'),
                'jam_member_9':request.form.get('jam_member_9'),
                'jam_member_10':request.form.get('jam_member_10'),
                'member_instrument_1':request.form.get('member_instrument_1'),
                'member_instrument_2':request.form.get('member_instrument_2'),
                'member_instrument_3':request.form.get('member_instrument_3'),
                'member_instrument_4':request.form.get('member_instrument_4'),
                'member_instrument_5':request.form.get('member_instrument_5'),
                'member_instrument_6':request.form.get('member_instrument_6'),
                'member_instrument_7':request.form.get('member_instrument_7'),
                'member_instrument_8':request.form.get('member_instrument_8'),
                'member_instrument_9':request.form.get('member_instrument_9'),
                'member_instrument_10':request.form.get('member_instrument_10'),
                'jam_notes':request.form.get('jam_notes'),
                'jam_owner':session['username']
            })
        
        print(request.form)
        return redirect(url_for('get_jams'))
    
    return render_template('addjam.html',
    counties=mongo.db.counties.find(),
    username=session['username'],
    user_logged_in=user_logged_in,
    instruments=mongo.db.instruments.find(),
    instruments_2=mongo.db.instruments.find(),
    instruments_3=mongo.db.instruments.find(),
    instruments_4=mongo.db.instruments.find(),
    instruments_5=mongo.db.instruments.find(),
    instruments_6=mongo.db.instruments.find(),
    instruments_7=mongo.db.instruments.find(),
    instruments_8=mongo.db.instruments.find(),
    instruments_9=mongo.db.instruments.find(),
    instruments_10=mongo.db.instruments.find())
    
@app.route('/delete_jam/<jam_id>')
def delete_jam(jam_id):
    mongo.db.jam_or_event.remove({'_id': ObjectId(jam_id)})
    return redirect(url_for('get_jams'))

@app.route('/edit_jam/<jam_id>', methods=['POST', 'GET'])
def edit_jam(jam_id):
    user_logged_in = 'username' in session
    the_jam =  mongo.db.jam_or_event.find_one({"_id": ObjectId(jam_id)})
    username=session['username']
    jam_owner = the_jam['jam_owner']
    
    if request.method == 'POST':
        if user_logged_in:
            if username == jam_owner:
                print(request.form)
                jams = mongo.db.jam_or_event
                jams.update( {'_id': ObjectId(jam_id)},
                {
                    'jam_title':request.form.get('jam_title'),
                    'genre':request.form.get('genre'),
                    'date_of_jam': request.form.get('date_of_jam'),
                    'jam_location': request.form.get('jam_location'),
                    'jam_county':request.form.get('jam_county'),
                    'jam_member_1':request.form.get('jam_member_1'),
                    'jam_member_2':request.form.get('jam_member_2'),
                    'jam_member_3':request.form.get('jam_member_3'),
                    'jam_member_4':request.form.get('jam_member_4'),
                    'jam_member_5':request.form.get('jam_member_5'),
                    'jam_member_6':request.form.get('jam_member_6'),
                    'jam_member_7':request.form.get('jam_member_7'),
                    'jam_member_8':request.form.get('jam_member_8'),
                    'jam_member_9':request.form.get('jam_member_9'),
                    'jam_member_10':request.form.get('jam_member_10'),
                    'member_instrument_1':request.form.get('member_instrument_1'),
                    'member_instrument_2':request.form.get('member_instrument_2'),
                    'member_instrument_3':request.form.get('member_instrument_3'),
                    'member_instrument_4':request.form.get('member_instrument_4'),
                    'member_instrument_5':request.form.get('member_instrument_5'),
                    'member_instrument_6':request.form.get('member_instrument_6'),
                    'member_instrument_7':request.form.get('member_instrument_7'),
                    'member_instrument_8':request.form.get('member_instrument_8'),
                    'member_instrument_9':request.form.get('member_instrument_9'),
                    'member_instrument_10':request.form.get('member_instrument_10'),
                    'jam_notes':request.form.get('jam_notes'),
                    'jam_owner':session['username']
                })
                return redirect(url_for('get_jams'))
                
            print(request.form)
            jams = mongo.db.jam_or_event
            jams.update( {'_id': ObjectId(jam_id)},
            {
                'jam_member_1':request.form.get('jam_member_1'),
                'jam_member_2':request.form.get('jam_member_2'),
                'jam_member_3':request.form.get('jam_member_3'),
                'jam_member_4':request.form.get('jam_member_4'),
                'jam_member_5':request.form.get('jam_member_5'),
                'jam_member_6':request.form.get('jam_member_6'),
                'jam_member_7':request.form.get('jam_member_7'),
                'jam_member_8':request.form.get('jam_member_8'),
                'jam_member_9':request.form.get('jam_member_9'),
                'jam_member_10':request.form.get('jam_member_10'),
                'member_instrument_1':request.form.get('member_instrument_1'),
                'member_instrument_2':request.form.get('member_instrument_2'),
                'member_instrument_3':request.form.get('member_instrument_3'),
                'member_instrument_4':request.form.get('member_instrument_4'),
                'member_instrument_5':request.form.get('member_instrument_5'),
                'member_instrument_6':request.form.get('member_instrument_6'),
                'member_instrument_7':request.form.get('member_instrument_7'),
                'member_instrument_8':request.form.get('member_instrument_8'),
                'member_instrument_9':request.form.get('member_instrument_9'),
                'member_instrument_10':request.form.get('member_instrument_10'),
                'jam_title':request.form.get('jam_title'),
                'genre':request.form.get('genre'),
                'date_of_jam': request.form.get('date_of_jam'),
                'jam_location': request.form.get('jam_location'),
                'jam_county':request.form.get('jam_county'),
                'jam_notes':request.form.get('jam_notes'),
                'jam_owner':request.form.get('jam_owner')
            })
            return redirect(url_for('get_jams'))
    if username == jam_owner:
        return render_template('editjam.html',
        jam=the_jam,
        instruments=mongo.db.instruments.find(),
        instruments_2=mongo.db.instruments.find(),
        instruments_3=mongo.db.instruments.find(),
        instruments_4=mongo.db.instruments.find(),
        instruments_5=mongo.db.instruments.find(),
        instruments_6=mongo.db.instruments.find(),
        instruments_7=mongo.db.instruments.find(),
        instruments_8=mongo.db.instruments.find(),
        instruments_9=mongo.db.instruments.find(),
        instruments_10=mongo.db.instruments.find(),
        counties=mongo.db.counties.find(),
        username=session['username'])
    return render_template('guesteditjam.html',
        jam=the_jam,
        instruments=mongo.db.instruments.find(),
        instruments_2=mongo.db.instruments.find(),
        instruments_3=mongo.db.instruments.find(),
        instruments_4=mongo.db.instruments.find(),
        instruments_5=mongo.db.instruments.find(),
        instruments_6=mongo.db.instruments.find(),
        instruments_7=mongo.db.instruments.find(),
        instruments_8=mongo.db.instruments.find(),
        instruments_9=mongo.db.instruments.find(),
        instruments_10=mongo.db.instruments.find(),
        counties=mongo.db.counties.find(),
        username=session['username'])
        
#login system - As the project brief does not require a login system, I have not hashed passwords

@app.route('/')
def index():
    users = mongo.db.users
    user_logged_in = 'username' in session
    if user_logged_in:
        return render_template('jams.html',
        jams=mongo.db.jam_or_event.find(),
        counties=mongo.db.counties.find(),
        username=session['username'])

    return render_template('jams.html',
        jams=mongo.db.jam_or_event.find(),
        counties=mongo.db.counties.find(),
        genres=mongo.db.genres.find())

@app.route('/login', methods=['POST', 'GET'])
def login():
    user_logged_in = 'username' in session
    if request.method == 'POST':
        users = mongo.db.users
        password = request.form['password']
        login_user = users.find_one({'username' : request.form['username']})
            
        if login_user:
            if password == login_user['password']:
                session['username'] = request.form['username']
                return redirect(url_for('get_jams'))
    
        return render_template('re-login.html')
        
    if user_logged_in:
        session.clear()
        return redirect(url_for('get_jams'))
    
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
            users.insert({'username' : request.form['username'], 
            'password' : request.form['password'], 
            'user_county' : request.form['user_county'],
            'user_instrument' : request.form['user_instrument']})
            session['username'] = request.form['username']
            return redirect(url_for('get_jams'))
        
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
