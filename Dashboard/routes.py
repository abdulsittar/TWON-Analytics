from flask import Blueprint
from flask import render_template, request, url_for, redirect, send_from_directory, jsonify, make_response

dashboard_bp = Blueprint(
    'Dashboard', __name__,
    template_folder='templates',
    static_folder='static'
)

@dashboard_bp.route('/')
def dashboard():
    print("ad dashboard")
    return render_template('layouts/default.html', content=render_template('pages/index.html'))

@dashboard_bp.route('/index')
def index():
    print("index")
    return render_template('layouts/default.html', content=render_template('pages/index.html'))

@dashboard_bp.route("/delhi/projects")
def donorschoose_projects():
    client = MongoClient('mongodb+srv://abdulsittar72:2106010991As@cluster0.gsnbbwq.mongodb.net/?retryWrites=true&w=majority')
    db = client.test
    users = db.users
    projects = users.find(projection=FIELDS, limit=10000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects, default=json_util.default)
    connection.close()
    return json_projects