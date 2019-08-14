import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import secrets 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = "Jamtree"
app.config["MONGO_URI"] = (
    "mongodb+srv://root:%s@myfirstcluster-8h2g0.mongodb.net/Jamtree?retryWrites=true&w=majority"
    ) %secrets.MONGOPASSWORD

mongo = PyMongo(app)

#CRUD

@app.route('/get_jams')
def get_jams():
    """ This works as the homepage, and shows all the existing jams in the database. """
    
    user_logged_in = 'username' in session
    if user_logged_in:
        # If the user is logged in, display their username as well as allow them to edit a jam #
        return render_template(
            "jams.html",
            jams=mongo.db.jam_or_event.find(),
            username=session['username'],
            user_logged_in=user_logged_in
            )

    return render_template(
        "jams.html",
        jams=mongo.db.jam_or_event.find(),
        user_logged_in=user_logged_in
        )

@app.route('/get_users')
def get_users():
    """ This shows all the existing users in the database. """
    
    user_logged_in = 'username' in session
    if user_logged_in:
        # If the user is logged in, show username in navbar #
        return render_template(
            "users.html",
            users=mongo.db.users.find(),
            username=session['username'],
            user_logged_in=user_logged_in
            )

    return render_template(
        "users.html",
        users=mongo.db.users.find(),
        user_logged_in=user_logged_in
        )

@app.route('/add_jam', methods=['POST', 'GET'])
def add_jam():
    """ This brings up, and posts the form to create a new jam. """

    user_logged_in = 'username' in session
    if request.method == 'POST':
        # This submits the form, creating the object #
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
        
        return redirect(url_for('get_jams'))
    
    # This brings up the form to create a new jam #
    return render_template(
        'addjam.html',
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
    """ This deletes a jam """
    
    mongo.db.jam_or_event.remove({'_id': ObjectId(jam_id)})
    return redirect(url_for('get_jams'))

@app.route('/edit_jam/<jam_id>', methods=['POST', 'GET'])
def edit_jam(jam_id):
    """ This route determines if you are the creator of the jam, and brings up the relevant edit page. """
    
    user_logged_in = 'username' in session
    the_jam =  mongo.db.jam_or_event.find_one({"_id": ObjectId(jam_id)})
    username=session['username']
    jam_owner = the_jam['jam_owner']
    
    if request.method == 'POST':
        if user_logged_in:
            if username == jam_owner:
                # Updating Jam if the user is also the jam creator #
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
            
            # Posts the updates for those who didn't create the jam #    
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
    # If the user is the creator of this particular jam, this allows you to edit more #        
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
        
    # This is for users to edit some details if they haven't created the jam #    
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
    """ This is used to redirect users who have logged in """
    users = mongo.db.users
    user_logged_in = 'username' in session
    if user_logged_in:
        return render_template('jams.html',
        jams=mongo.db.jam_or_event.find(),
        counties=mongo.db.counties.find(),
        username=session['username'],
        user_logged_in=user_logged_in)

    return render_template('jams.html',
        jams=mongo.db.jam_or_event.find(),
        counties=mongo.db.counties.find(),
        genres=mongo.db.genres.find(),
        user_logged_in=user_logged_in)

@app.route('/login', methods=['POST', 'GET'])
def login():
    """ This is the login system: PLEASE NOTE - the passwords are saved raw, as this was not in the scope of the project brief """
    user_logged_in = 'username' in session
    if request.method == 'POST':
        users = mongo.db.users
        password = request.form['password']
        login_user = users.find_one({'username' : request.form['username']})
            
        if login_user:
        # If the usename entered matches to a username on the database #
            if password == login_user['password']:
                # If the password entered matches the password for this user, save username to session and 'login' #
                session['username'] = request.form['username']
                return redirect(url_for('get_jams'))
        
        # If the password or username didn't match, request they try again #
        return render_template('re-login.html')
    # render the login page #
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    """ This is the registration route, that creates a user and saves their details. """
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username' : request.form['username']})

        if existing_user is None:
        # If there is no existing users that matches the username entered #
            users.insert({'username' : request.form['username'], 
            'password' : request.form['password'], 
            'user_county' : request.form['user_county'],
            'user_instrument' : request.form['user_instrument']})
            session['username'] = request.form['username']
            return redirect(url_for('get_jams'))
        
        return render_template(
            're-register.html',
            instruments=mongo.db.instruments.find()
            )

    return render_template('register.html',
    instruments=mongo.db.instruments.find(),
    counties=mongo.db.counties.find())

if __name__ == '__main__':
    app.secret_key = secrets.APP_SECRET
    app.run(host=os.environ.get('IP'),
            port=int(8080),
            debug=True)
