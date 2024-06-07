from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus
password = quote_plus('Y9&ZvR4*2?BdNp')
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mssql+pyodbc://sa:{password}@mssql-database-service:1433/contacts_db?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Contact(db.Model):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(80), nullable=False)  # Use Unicode
    surname = db.Column(db.Unicode(100), nullable=True)  # Use Unicode
    email = db.Column(db.Unicode(200), nullable=True, unique=True)  # Use Unicode
    phone = db.Column(db.Unicode(20), nullable=True, unique=False) 

    def __repr__(self):
        return '<Contacts %r>' % self.name
