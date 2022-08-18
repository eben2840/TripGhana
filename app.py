
from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from crypt import methods
from flask import Flask, redirect, render_template, url_for,request
from forms import *
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
migrate= Migrate(app, db)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return f"Course('{self.id}', {self.id}', )"


@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('ent.html')
    return render_template('ent.html')

@app.route('/second')
def second():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('head.html')
    return render_template('head.html')

@app.route('/third')
def third():
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


@app.route('/blog')
def blog():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('blog.html')
    return render_template('blog.html')

    
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

    
@app.route('/six')
def six():
    names=Course.query.all()
    print(names)
    return render_template('venue.html', names=names)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=50000,debug=True)
