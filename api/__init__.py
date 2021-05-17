import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CONNECTION_STRING = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'
db_username = os.environ['GRAPHQL_TUTORIAL_DB_USER']
db_password = os.environ['GRAPHQL_TUTORIAL_DB_PASSWORD']
db_host = os.environ['GRAPHQL_TUTORIAL_DB_SERVER']
db_name = os.environ['GRAPHQL_TUTORIAL_DB_NAME']
app.config["SQLALCHEMY_DATABASE_URI"] = CONNECTION_STRING.format(user=db_username, password=db_password, server=db_host, database=db_name)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello!'
