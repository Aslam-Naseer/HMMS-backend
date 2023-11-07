from CRUD import fetcher,insertor
from connect import connector
from flask_cors import CORS
import json 
from flask import Flask , request, jsonify ,session

app = Flask(__name__)
app.secret_key = "909090"
CORS(app)
# conn=None

# global conn

conn,_=connector()

@app.route('/')
def home():
    return "flask home"

@app.route('/list')
def list():
    global conn
    
    query = """SELECT * FROM inmate;"""
    data=fetcher(conn,query)
    
    return data

@app.route('/userreg' ,methods=['POST','GET'])
def reg_user():
    # from post data
    data =request.json
    print(data['hostelid'],data['password'])
    global conn
    hostelid =data['hostelid']
    password =data['password']
    query = f"INSERT INTO User_det (inmate_id, password) VALUES ('{hostelid}', '{password}');"
    insertor(conn,query)    
    response_data = {'message': 'Data received successfully', 'status': 200}
    return jsonify(response_data)


@app.route('/userlog' ,methods=['POST','GET'])
def log_user():
    
    data =request.json
    print(data['hostelid'],data['password'])
    hostelid =data['hostelid']
    password =data['password']
    if hostelid == 'admin' and password == 'admin':
        session['userid'] = hostelid
        response_data = {'message': 'Data received successfully', 'status': 200}
        return jsonify(response_data)


@app.route('/userlogout' )
def logout_user():
    uid=session.get('userid', None)
    session.pop('userid', None)
    response_data = {'message': "log out successfull", 'status': 200}
    return jsonify(response_data)






if __name__ == '__main__':
    app.run(debug=True)