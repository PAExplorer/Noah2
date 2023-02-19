from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/path/to/uploads'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check the username and password.
        username = request.form['username']
        password = request.form['password']
        if username != 'myusername' or password != 'mypassword':
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