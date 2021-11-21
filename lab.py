from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask import request
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = 'password'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Students(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = False)
    name = db.Column(db.String(80), nullable=False)
    stream = db.Column(db.String(80), nullable=False)
    def __init__(self,i, n, s):
        self.id = i
        self.name = n
        self.stream = s


@app.route('/create', methods = ['POST'])
def create():
    data = request.get_json()
    id = data['id']
    name = data['name']
    stream = data['stream']
    result = Students.query.filter_by(id=id).first()
    if(result):
        return "id already exists"
    else:
        data = Students(id,name,stream)
        db.session.add(data)
        db.session.commit()
        return "added successfully"

@app.route('/read', methods = ['GET'])
def read():
    data = Students.query.all()
    result = {}
    for i in data:
        result[i.id] = {'name':i.name, 'stream': i.stream}
    return result

@app.route('/update', methods = ['PUT'])
def update():
    data = request.get_json()
    id = data['id']
    name = data['name']
    stream = data['stream']
    check = Students.query.filter_by(id=id).first()
    if (check):
        check.name = name
        check.stream = stream
        db.session.commit()
        return 'Update Success'
    else:
        return 'id not found'
    


@app.route('/delete/<int:id>', methods = ['DELETE'])
def delete(id):
    check = Students.query.filter_by(id=id).first()
    if check is not None:
        db.session.delete(check)
        db.session.flush()
        db.session.commit()
        return 'Delete Success'
    else:
        return 'id not found'

db.create_all()
app.run(port=8000,debug=True)