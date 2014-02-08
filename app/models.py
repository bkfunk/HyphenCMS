from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    
class Piece(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text())
    text = db.Column(db.Text())
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))