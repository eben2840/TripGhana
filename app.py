from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request
from flask_login import login_required,login_user,logout_user,current_user,UserMixin, LoginManager
from forms import *
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
migrate= Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
migrate = Migrate(app, db)
from forms import *

@login_manager.user_loader
def load_user(user_id):
    return Course.query.get(int(user_id))



class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=True)
    name = db.Column(db.String(), nullable=True)
    
    comment = db.Column(db.String(), nullable=True)
    
    def __repr__(self):
        return f"Course('{self.id}', {self.email}', {self.comment}')"


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('ent.html')
    return render_template('ent.html')

@app.route('/about')
def about():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('head.html')
    return render_template('head.html')

@app.route('/event')
def event():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('photo.html')
    return render_template('photo.html')

@app.route('/four')
def four():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('phone.html')
    return render_template('phone.html')


@app.route('/promotion')
def promotion():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('blog.html')
    return render_template('blog.html')

@app.route('/ourteam')
def outteam():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('debit.html')
    return render_template('debit.html')

'''  
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if request.method=='POST':
        
        print(form.username.data)
        print(form.password.data)
        namelogin=Course(name=form.username.data)
        db.session.add(namelogin)
        db.session.commit()
        # Handle POST Request here
        return redirect(url_for('six'))
    return render_template('signup.html', form=form)
'''
''''
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    name=Course.query.get_or_404(id)
    form = RegistrationForm()
    form.username.data=name.name
    if request.method=='POST':
        print(form.username.data)
        print(form.password.data)
        namelogin=Course(name=form.username.data)
        db.session.add(namelogin)
        db.session.commit()
        # Handle POST Request here
        return redirect(url_for('six'))
    return render_template('signup.html', form=form)
'''
@app.route('/comment')
def comment():
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
    return render_template("comment.html", persons=persons)

@app.route('/heads')
def heads():
    return render_template("heads.html")

@app.route('/blogg')
def blogg():
    return render_template("blogg.html")

@app.route('/form')
def form():
    return render_template("form.html")
  
@app.route('/index' , methods=['POST', 'GET'])
def index():
    form = RegistrationForm()
    if request.method=='POST':
        print(form.name.data)
     
        newentry=Course(name=form.name.data)
        db.session.add(newentry)
        db.session.commit()
        print("successful")
        return redirect("/hom")
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
    
    
    return render_template("index.html", form=form, persons=persons)
   

@app.route('/hom', methods=['POST','GET'])
def hom():
    form = RegistrationForm()
    if request.method=='POST':
        print(form.email.data)
        print(form.comment.data)
        newentry=Course(email=form.email.data, comment=form.comment.data)
        db.session.add(newentry)
        db.session.commit()
        print("successful")
        return redirect("/hom")
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
    print(current_user)
    
    return render_template("venue.html", form=form, persons=persons, current_user=current_user)

@app.route("/delete/<int:id>")
def delete(id):
    delete=Course.query.get_or_404(id)
    try:
            db.session.delete(delete)
            db.session.commit()
            return redirect('/comment') 
    except: 
        return "errrrrorrr"
 
 
@app.route('/hotel')
def hotel():
    return render_template('hotel.html')


@app.route('/rest')
def rest():
    return render_template('rest.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=3000,debug=True)
