from flask import Flask
from importlib import import_module
import os
import configparser
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from Dashboard import routes

app = Flask(__name__, static_url_path="/static", static_folder= "/Dashboard/static")

app.register_blueprint(routes.dashboard_bp)

client = MongoClient('mongodb+srv://abdulsittar72:2106010991As@cluster0.gsnbbwq.mongodb.net/?retryWrites=true&w=majority')

db = client.test
users = db.users

print(users)
print(app.url_map)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    


