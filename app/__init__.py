from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.admin import Admin
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
Bootstrap(app)

from app import views, models

admin = Admin(app, name = "HyphenAdmin")
admin.add_view(views.PieceAdminView(models.Piece, db.session,  endpoint='pieces'))
admin.add_view(views.AdminView(models.Item, db.session, endpoint='items'))
admin.add_view(views.AdminView(models.Author, db.session, endpoint='authors'))
admin.add_view(views.GenreAdminView(models.Genre, db.session, endpoint='genres'))
