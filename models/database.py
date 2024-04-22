from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Padaria(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    quantidade = db.Column(db.Integer)
    preco = db.Column(db.Float)

    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco