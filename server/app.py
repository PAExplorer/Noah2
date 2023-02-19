from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

db = SQLAlchemy() #Initialize database
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cred.db' #refer to the sql database locally with our app.py not sure if three / are needed so I am going with two for now
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check the username and password.
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return render_template('login.html', error='Invalid username or password')
        
        # Check if the file is in the request.
        if 'file' not in request.files:
            return render_template('upload.html', error='No file selected')
        
        # Get the file from the request and save it to disk.
        file = request.files['file']
        if file.filename == '':
            return render_template('upload.html', error='No file selected')
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return redirect(url_for('success'))
    
    return render_template('login.html')

@app.route('/success')
def success():
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)