enter the virtual environment with the command:

source venv/bin/activate

similarly to exit:

deactivate



Flash should be installed in this virtual environment with:

pip install Flask
pip install flask_sql_alchemy
pip install config

(Eventually these will be added to a requirements.txt file but since the list is still growing it's remaining here.)



Run the development server with the command in the VENV:

python -m flask run



Furthermore your linux should have SQLite database creation methods. In our case sqlite3 is installed via:

sudo apt install sqlite3 

We use sqlite3 to create the database cred.db with the following definitions:
CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL);
INSERT INTO users (username, password) VALUES ('user1', 'password1');
INSERT INTO users (username, password) VALUES ('user2', 'password2');


TO DO:

add uploda progress bar

create method for admin to create and remove username and password hashes