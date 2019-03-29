from flask import Flask
from os import getenv
from api.data import dataAPI
import sqlite3

app = Flask(__name__)
app.register_blueprint(dataAPI)

env_port = getenv('PORT')
port = 5000 if not env_port else env_port

if __name__ == '__main__':
    conn = sqlite3.connect('data/accounts.db')
    # print(port)
    # print("this is a test")
    app.run('0.0.0.0', int(port), debug=True, threaded=True)