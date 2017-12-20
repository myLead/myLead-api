from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://matyyaxexjsmlg:8107604602e55661da27d1cac9e0ab04651a87ac4e6846101ca391cb383199c3@ec2-107-20-176-7.compute-1.amazonaws.com:5432/de7q9p7jklnn70'
db = SQLAlchemy(app)

from usuarioAPI import *
from dbhelper import * 


if __name__ == '__main__':
   
    app.run(debug=True)
    
    