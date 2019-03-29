from flask import Blueprint, jsonify, request
import sqlite3

dataAPI = Blueprint('dataAPI', __name__)

@dataAPI.route('/data', methods = ['GET','POST'])
def data():
    methodName = request.method
    if methodName == 'GET':
        findData(request)
        
    elif methodName == 'POST':
        task = getData(request)
        addNewAccount(task)
    return ""

def getData(reqest):
    try:
        name = request.form['Name'] # this will get data from the body section
    except KeyError:
        name = ""

    try:
        admin = request.form['Admin']
    except KeyError:
        admin = "No"

    try:
        contact = request.form['Contact']
    except KeyError:
        contact = "*@*.com"

    return (name, admin, contact)

def addNewAccount(task):
    conn = sqlite3.connect('data/accounts.db')
    c = conn.cursor()
    sql = "INSERT INTO accounts (name,admin,contact) values(?,?,?)"
    c.execute(sql, task)
    conn.commit()
    conn.close()

def findData(request):
    conn = sqlite3.connect('data/accounts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM accounts")
    rows = c.fetchall()

    print(request.args)
    print(rows)