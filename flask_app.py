from CRUD import fetcher,insertor,user_search
from connect import connector
from flask_cors import CORS
import json 
from flask import Flask , request, jsonify ,session

app = Flask(__name__)
app.secret_key = 'super secret key'
CORS(app)
# conn=None

# global conn 
# just checking

conn,_=connector()

@app.route('/')
def home():
    
    return "flask home"

# @app.route('/list',methods=['POST','GET'])
# def list():
#     global conn
#     id=request.json['hostelid']
#     print(type(id))
#     query = f"SELECT * FROM inmate where inmate_id = '{id}';"
#     print(query)
#     data=fetcher(conn,query)
    
    return data

@app.route('/userreg' ,methods=['POST','GET'])
def reg_user():
    global conn
    conn,_=connector()
    # from post data
    data =request.json
    # print(data)
    
    # print(data['hostelid'],data['password'])
    hostelid =data['hostelid'].upper()
    password =data['password'].upper()
    if hostelid !='' and password !='':
        query1 = f"SELECT * FROM user_det where inmate_id = '{hostelid}';"
        data1 =fetcher(conn,query1)
        print(data1)
        if data1 ==[]:
            query = f"INSERT INTO User_det (inmate_id, password) VALUES ('{hostelid}', '{password}');"
            insertor(conn,query)
            response_data = {'message': 'Data received successfully', 'status': 200}
            return jsonify(response_data)
        else:
            response_data = {'message': 'User already exits', 'status': 404}
            return jsonify(response_data)
    else:
        response_data = {'message': 'Data not received', 'status': 405  }
        return jsonify(response_data)


@app.route('/userlog' ,methods=['POST','GET'])
def log_user():
    conn,_=connector()
    data =request.json
    
    hostelid =data['hostelid'].upper()
    password =data['password'].upper()
    if hostelid =='' or password =='':
        response_data = {'message': 'Data not received', 'status': 405  }
        return jsonify(response_data)
    query = f"SELECT * FROM user_det where inmate_id ='{hostelid}' and password ='{password}';"

    
    # print(query)
    data =user_search(conn,query)
    
    if hostelid == data[0] and password == data[1]:
        response_data = {'key':hostelid,'message': 'User logged in successfully', 'status': 200}
        return jsonify(response_data)
        
    else:
        response_data = {'message': 'Login Unsuccessfull', 'status': 404}
        return jsonify(response_data)

@app.route('/userlogout' )
def logout_user():
    uid=session.get('userid', None)
    session.pop('userid', None)
    response_data = {'message': "log out successfull", 'status': 200}
    return jsonify(response_data)

@app.route('/dash' ,methods=['GET','POST'])
def dash():
    conn,_=connector()
    key =request.json
    id=key['hostelid']
    id=id.upper()
    query = f"SELECT * FROM inmate where hostel_id = '{id}';"
    data =fetcher(conn,query)
    
    return data






if __name__ == '__main__':
    app.run(debug=True)