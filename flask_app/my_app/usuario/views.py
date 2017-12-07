import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.usuario.models import Usuario
 
api = Blueprint('api', __name__)
 
@api.route('/')
@api.route('/home')
def home():
    return "Welcome to the app Home."
 
 
class UsuarioView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            usuarios = Usuario.query.paginate(page, 10).items
            res = {}
            for usuario in usuarios:
                res[usuario.id] = {
                    "nome": usuario.nome_usuario,
                    "email": usuario.email_usuario,
                    "senha": usuario.senha_usuario,
                }
        else:
            usuario = Usuario.query.filter_by(id=id).first()
            if not usuario:
                abort(404)
            res = {
                "nome": usuario.nome_usuario,
                "email": usuario.email_usuario,
                "senha": usuario.senha_usuario,
            }
        return jsonify(res)
 
    def post(self):
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        usuario = Usuario(nome, email, senha)
        db.session.add(usuario)
        db.session.commit()
        return jsonify({usuario.id: {
            "nome": usuario.nome_usuario,
            "email": usuario.email_usuario,
            "senha": usuario.senha_usuario,
        }})
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        return
 
    def delete(self, id):
        # Delete the record for the provided id.
        return
 
 
usuario_view =  UsuarioView.as_view('usuario_view')
app.add_url_rule(
    '/usuario/', view_func=usuario_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/usuario/<int:id>', view_func=usuario_view, methods=['GET']
)