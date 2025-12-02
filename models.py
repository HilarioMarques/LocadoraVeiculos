from config import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="cliente")

    locacoes = db.relationship(
        "Locacao",
        back_populates="usuario",
        foreign_keys="Locacao.usuario_id"
    )

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)


class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(20), unique=True, nullable=False)
    marca = db.Column(db.String(100))
    modelo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(50))
    preco_diaria = db.Column(db.Numeric(10,2), default=0.00)
    status = db.Column(db.Enum('disponivel','reservado','alugado','manutencao'), default='disponivel')
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    locacoes = db.relationship("Locacao", backref="veiculo", lazy=True)


class Locacao(db.Model):
    __tablename__ = "locacoes"

    id = db.Column(db.Integer, primary_key=True)

    # Cliente
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    usuario = db.relationship(
        "Usuario",
        back_populates="locacoes",
        foreign_keys=[usuario_id]
    )

    # Funcionário solicitante
    solicitante_funcionario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    solicitante = db.relationship(
        "Usuario",
        foreign_keys=[solicitante_funcionario_id]
    )

    veiculo_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime, nullable=False)
    valor_total = db.Column(db.Numeric(10,2))
    status = db.Column(db.Enum('pendente','confirmada','rejeitada','ativa','finalizada','cancelada'),
                       default='pendente')
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
