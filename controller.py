from flask import Flask, request, jsonify, render_template
from model import *
import hashlib
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/teste1'

db.init_app(app)

@app.route('/create')
def create():
    db.create_all()
    return 'Tablelas criadas'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['GET'])
def get_all_users():

    users = User.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['public_id'] = user.public_id
        user_data['name'] = user.name
        user_data['password'] = user.password
        user_data['admin'] = user.admin
        output.append(user_data)

    return jsonify({'users' : output})

@app.route('/user/<id>' , methods = ['GET'])
def get_one_user(id):

    

    user = User.query.filter_by(id=id).first()

    if not user:
        return jsonify({'messege' : 'No user found!'})
    user_data = {}
    user_data['id'] = user.id
    user_data['public_id'] = user.public_id
    user_data['name'] = user.name
    user_data['password'] = user.password
    user_data['admin'] = user.admin

    return jsonify({'user' : user_data})

@app.route('/user', methods =['POST'])
def create_user():
    

    data = request.get_json()
    teste = data['password']
    passw = hashlib.md5()
    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()
    print(hash)
    
    

    hashed_password = generate_password_hash(data['password'], method='sha256')

    new_user = User(public_id=str(uuid.uuid4()), name=data['name'], password=hash, admin=data['admin'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})

@app.route('/user/<use_id>', methods=['put'])
def promote_user():
    return ''

@app.route('/user/<id>', methods = ['DELETE'])
def delete_user(id):

    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify({'messege' : 'No user found"'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'messege' : 'User has been Deleted" '})


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()

