from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://get-it-done:get-it-done@localhost:8889/get-it-done'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

app.secret_key = 'jpfsop0495nfuianrgp019283iuern0n87unrnub098346ounb'

class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)   #every persistent class will need to have an id for database insertion
    name = db.Column(db.String(120))   #creating column 'name' with 120 characters maximum
    completed = db.Column(db.Boolean)
    #owner_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __init__(self, name):
        self.name = name
        self.completed = False
        self.owner = owner

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    useremail = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, useremail, password):
        self.useremail = useremail
        self.password = password

@app.before_request
def require_login():
    allowed_routes = ['login', 'register']

    if request.endpoint not in allowed_routes and 'useremail' not in session:
        return redirect('/login')

@app.route('/', methods=['POST', 'GET', 'PUT'])   #PUT method is used for updates from form data
def index():

    if request.method == 'POST':
        task_name = request.form['task']   #request.form.get will return "None" and allow better handling of any error... I need to try using this again...
        new_task = Task(task_name)   #instantiation of the substantiated class, the parameters of the class must be passed thru in order to be valid
        db.session.add(new_task)
        db.session.commit()
    
    tasks = Task.query.filter_by(completed=False).all()
    completed_tasks = Task.query.filter_by(completed=True).all()

    return render_template('todos.html', title="To Do List", tasks=tasks, completed_tasks=completed_tasks)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(useremail=email).first()

        if user and user.password == password:
            session['useremail'] = email
            return redirect('/')
        else:
            return '<p>Error!</p>'
    
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        verify = request.form['verify_password']

        existing_user = User.query.filter_by(useremail=email).first()

        if not existing_user:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            session['useremail'] = email
            
            return redirect ('/')
        else:
            return '<p>Duplicate User</p>'

    return render_template('register.html')

@app.route('/delete-task', methods=['POST'])   #could use a delete method in the form and add methods=['DELETE'] here in the code
def delete_task():

    task_id = int(request.form['task-id'])
    task = Task.query.get(task_id)
    task.completed = True
    db.session.add(task)
    db.session.commit()

    return redirect('/')

@app.route('/logout')
def logout():
    del session['useremail']

    return redirect('/')

if __name__ == '__main__':
    app.run()