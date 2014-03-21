from app import app, db
from models import Piece, Item, Author
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.model.template import macro
from flask.ext.admin.form import rules
from flask import render_template, flash, redirect, session, url_for, request, g
import pdb

@app.route('/')
@app.route('/index')
def index():
    pieces = Piece.query.all()
    return render_template('index.html', pieces = pieces)
    
class AdminView(ModelView):
    pass

class GenreAdminView(ModelView):
    form_create_rules = ('title', 'slug', 'markup')
    
class PieceAdminView(ModelView):
    column_list = ('publish_date', 'author', 'genre', 'items')
    list_template = 'admin/piece_list.html'
    inline_models = (Item,)
    column_formatters = dict(items = macro('render_items'),
                             author = macro('render_author'),
                             genre = macro('render_genre'))
    #print locals
        #print(db.session.query(Item).filter_by(piece_id = id).all())
    #columns_select_related_list = (Piece.items)
    #column_auto_select_related = True
    """def get_query(self):
        return self.session.query(self.model)
    def get_count_query(self):
        return self.session.query(func.count('*')).select_from(self.model)"""
        