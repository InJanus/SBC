from flask import Blueprint, jsonify, request
import sqlite3

dataAPI = Blueprint('dataAPI', __name__)

@dataAPI.route('/data', methods = ['GET','POST'])
def data():
    methodName = request.method
    if methodName == 'GET':
        mydata = findData(request)
        return jsonify(mydata)
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

def exQ(c ,query):
    c.execute(query)
    return c.fetchall()

def findData(request):
    conn = sqlite3.connect('data/accounts.db')
    c = conn.cursor()
    rows = exQ(c,"SELECT * FROM accounts")
    rawtableNames = exQ(c, "PRAGMA table_info(accounts)")

    terms = []
    for i in rawtableNames:
        terms.append(i[1].lower())

    output = []
    #this has to be able to search for the data that i need. maybe in the future i can get any data t be added.
    for j in terms:
        for i in rows:
            try:
                if i[terms.index(j)] == request.args[j]:
                    output.append(i)
            except KeyError:
                pass
    if output:
        return output
    else:
        return {'data':'Search Unsucessful'}
