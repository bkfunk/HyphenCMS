from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(120))
    middlename = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    email = db.Column(db.String(120), index = True, unique = True)
    slug = db.Column(db.String(120), index = True, unique = True)
    bio = db.Column(db.Text())
    pieces = db.relationship('Piece', backref = 'author', lazy = 'dynamic')
    
    def __repr__(self):
        return '<Author %r, %r %r>' % (self.lastname, self.firstname, self.middlename)
        #return self.lastname + ', ' + self.firstname + ' ' + self.middlename
        
    def last_first_middle(self):
        return str(self.lastname) + ", " + str(self.firstname) + " " + str(self.middlename)
        
    def first_middle_last(self):
        return str(self.firstname) + (" " + self.middlename if str(self.middlename) else "") + " " + str(self.lastname)
    
    
class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text())
    slug = db.Column(db.String(120))
    abstract = db.Column(db.Text())
    abstract_style = db.Column(db.String(120))
    text = db.Column(db.Text())
    piece_id = db.Column(db.Integer, db.ForeignKey('piece.id'))
    #piece = db.relationship('Piece', backref='item_list')
    
    def __repr__(self):
        return '<Item %r>' % (self.title)

class Piece(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    publish_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    items = db.relationship('Item', backref = 'piece', lazy = 'dynamic')
    #author = db.relationship('Author')
        
    def __repr__(self):
        titles = map(lambda i: str(i.title), self.items.all())
        if self.author:
            author = self.author.last_first_middle()
        else:
            author = None
        return '<Piece %r: %s by %r>' % (self.id, titles, author)

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), index = True, unique = True)
    slug = db.Column(db.String(120), index = True, unique = True)
    markup = db.Column(db.String(240))
    pieces = db.relationship('Piece', backref = 'genre', lazy = 'dynamic')
    
    def __repr__(self):
        return '<Genre %r>' % (self.title)
    