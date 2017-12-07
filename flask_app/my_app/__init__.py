from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from my_app.usuario.views import api
app.register_blueprint(api)
 
db.create_all()