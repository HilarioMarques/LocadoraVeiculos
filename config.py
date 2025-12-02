from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Chave para uso de sessões
app.config["SECRET_KEY"] = "chave-super-secreta"

# Config MySQL (ajuste usuario e senha)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:#Karamazov777@localhost/locadora_db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
