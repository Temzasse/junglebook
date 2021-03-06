from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.heroku import Heroku

app = Flask(__name__)
app.config.from_object('config')
heroku = Heroku(app)
db = SQLAlchemy(app)

from app import models, views

# if __name__ == '__main__':
#     app.debug = False
#     app.run()

