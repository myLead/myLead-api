from flask_sqlalchemy import SQLAlchemy
from datetime         import datetime
from sqlalchemy       import ForeignKey
from sqlalchemy.orm   import relationship
from mylead           import db


class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id_usuario    = db.Column(db.Integer,     primary_key = True)
    nome          = db.Column(db.String(100), nullable    = False)
    email_usuario = db.Column(db.String(100), nullable    = False)
    senha_usuario = db.Column(db.String(80),  nullable    = False)
    cnpj          = db.Column(db.String(20),  nullable    = False)
    create_at     = db.Column(db.DateTime(),  index       = True, default = datetime.now)
    
    
class Compra(db.Model):
    __tablename__   = 'Compra'
    id_compra       = db.Column(db.Integer, primary_key=True)
    data_compra     = db.Column(db.Date())
    data_vencimento = db.Column(db.Date())
    id_usuario      = db.Column(db.INT(),   nullable=False)
    id_plano        = db.Column(db.INT(),   nullable=False)
    # id_Usuario = relationship("Usuario", cascade="save_update") 


class Plano(db.Model):
    __tablename__   = 'Plano'
    id_plano        = db.Column(db.Integer, primary_key=True)
    descricao_plano = db.Column(db.TEXT())
    valor           = db.Column(db.TEXT())


class Pessoa(db.Model):
    __tablename__    = 'Pessoa'
    id_pessoa        = db.Column(db.Integer,     primary_key = True)
    nome_pessoa      = db.Column(db.String(100), nullable    = False)
    email_pessoa     = db.Column(db.String(100), nullable    = False)
    telefone_usuario = db.Column(db.String(20),  nullable    = True)
    celular_pessoa   = db.Column(db.String(20),  nullable    = True)


class Empresa(db.Model):
    __tablename__ = 'Empresa'
    id_empresa    = db.Column(db.Integer,     primary_key = True)
    nome_empresa  = db.Column(db.String(100), nullable    = False)
    qtdps_empresa = db.Column(db.Integer,     nullable    = False)
    ramo_empresa  = db.Column(db.String(20),  nullable    = False)


class Eventos(db.Model):
    __tablename__     = 'Eventos'
    id_evento         = db.Column(db.Integer,     primary_key = True)
    descricao_evento  = db.Column(db.String(100), nullable    = False)
  

class Atividades(db.Model):
    __tablename__        = 'Atividades'
    id_atividade         = db.Column(db.Integer,     primary_key = True)
    descricao_atividade  = db.Column(db.String(100), nullable    = False)


class RedeSocial(db.Model):
    __tablename__  = 'RedeSocial'
    id_rede_social = db.Column(db.Integer,     primary_key = True)
    link_fck       = db.Column(db.String(200), nullable    = False)
    link_lkdn      = db.Column(db.String(200), nullable    = False)
    link_twt       = db.Column(db.String(200), nullable    = False)
    link_blog      = db.Column(db.String(200), nullable    = False)


class DonoLead(db.Model):
    __tablename__ = 'DonoLead'
    id_dono       = db.Column(db.Integer,     primary_key  = True)
    email_dono    = db.Column(db.String(100), nullable     = False)
    nome_dono     = db.Column(db.String(100), nullable     = True)


class Lead(db.Model):
    __tablename__       = 'Lead'
    id_lead             = db.Column(db.Integer,     primary_key = True)
    estg_funil_lead     = db.Column(db.String(100), nullable    = False)
    url_pblc_lead       = db.Column(db.String(100), nullable    = False)
    perfil_lead         = db.Column(db.String(100), nullable    = False)
    id_pessoa_lead      = db.Column(db.Integer, ForeignKey('Pessoa.id_pessoa'),          nullable    = False)
    id_empresa_lead     = db.Column(db.Integer, ForeignKey('Empresa.id_empresa'),        nullable    = False)
    id_rede_social_lead = db.Column(db.Integer, ForeignKey('RedeSocial.id_rede_social'), nullable    = False)
    id_dono_lead        = db.Column(db.Integer, ForeignKey('DonoLead.id_dono'),          nullable    = False)

    id_Pessoa = relationship("Pessoa",         back_populates = "id_pessoa_lead")
    id_Empresa = relationship("Empresa",       back_populates = "id_empresa_lead")
    id_RedeSocial = relationship("RedeSocial", back_populates = "id_rede_social_lead")
    id_Dono = relationship("Dono",             back_populates = "id_dono_lead")


class Atuacao(db.Model):
    __tablename__        = 'Atuacao'
    id_lead_atuacao      = db.Column(db.Integer, ForeignKey('Lead.id_lead'),            primary_key = True)
    id_atividade_atuacao = db.Column(db.Integer, ForeignKey('Atividades.id_atividade'), primary_key = True)

    id_Lead      = relationship("Lead",       back_populates = "id_lead_atuacao")
    id_Atividade = relationship("Atividades", back_populates = "id_atividade_atuacao")


class Participacao(db.Model):
    __tablename__          = 'Participacao'
    id_lead_participacao   = db.Column(db.Integer, primary_key = True)
    id_evento_participacao = db.Column(db.Integer, primary_key = True)

    id_Lead   = relationship("Lead",    back_populates = "id_lead_participacao")
    id_Evento = relationship("Evento",  back_populates = "id_evento_participacao")

