
from flask_sqlalchemy import SQLAlchemy
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
    email = db.Column(db.String(), nullable=True, unique=True)
    name = db.Column(db.String(), nullable=True, unique=True)
    comment = db.Column(db.String(), nullable=True)
    budget =db.Column(db.String())
    
    def __repr__(self):
        return f"Course('{self.id}', {self.email}', {self.comment}')"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    des = db.Column(db.String())
    incase = db.Column(db.String())
    image_file =db.Column(db.String())
    
    def __repr__(self):
        return f"Course('{self.id}', {self.name}')"


@app.route('/',methods=['GET','POST'])
def homee():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('ent.html')
    return render_template('ent.html')

@app.route('/base',methods=['GET','POST'])
def base():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('base.html')
    return render_template('base.html')

@app.route('/centralmall',methods=['GET','POST'])
def centralmall():
    add=Item.query.all()
    return render_template('about.html',add=add)

@app.route('/shop',methods=['GET','POST'])
def shop():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('shop.html')
    return render_template('shop.html')



@app.route('/kalitexcreatives',methods=['GET','POST'])
def kalitexcreatives():
    
    return render_template('kalitexcreativs.html')

@app.route('/vendor1',methods=['GET','POST'])
def vendor1():
    if request.method=='POST':
        return render_template('vendor1.html')
    return render_template('vendor1.html')
    
@app.route('/product',methods=['GET','POST'])
def product():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('product.html')
    return render_template('product.html')

@app.route('/contact1',methods=['GET','POST'])
def contact1():
    if request.method=='POST':
        return render_template('contact1.html')
    return render_template('contact1.html')

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


@app.route('/blog')
def blog():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('blog.html')
    return render_template('blog.html')

@app.route('/security')
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

@app.route('/heads')
def heads():
    return render_template("heads.html")


@app.route('/login', methods=["POST","GET"])
def login():
    return render_template("login.html")

@app.route('/sign', methods=["POST","GET"])
def sign():
    return render_template("sign.html")


@app.route('/signinn' , methods=["POST","GET"])
def signinn():
    return render_template("signinn.html")


@app.route('/budget', methods=['POST', 'GET'])
def index2():
    form = RegistrationForm()
    if request.method=='POST':
        print(form.name.data)
        print(form.budget.data)
     
        newentry=Course(name=form.name.data,budget=form.budget.data)
        db.session.add(newentry)
        db.session.commit()
        print("successful")
        return redirect("/home")
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
    
    
    return render_template("index2.html", form=form, persons=persons)


@app.route('/additem',methods=['GET','POST'])
def additem():
    form=Add()
  
    if form.validate_on_submit():
  
            new=Item(name=form.name.data,
                     des=form.des.data,
                     incase=form.incase.data,   
               image_file=form.image_file.data
                  )
       
            db.session.add(new)
            db.session.commit()
            
            return redirect('/centralmall')
    print(form.errors)
    return render_template("additem.html", form=form)
 



@app.route('/blogg')
def blogg():
    return render_template("additem.html")

@app.route('/form')
def form():
    return render_template("form.html")
  
@app.route('/welcome' , methods=['POST', 'GET'])
def welcome():
    form = RegistrationForm()
    if request.method=='POST':
        print(form.name.data)
     
        newentry=Course(name=form.name.data)
        db.session.add(newentry)
        db.session.commit()
        print("successful")
        return redirect("/home")
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
    
    
    return render_template("welcome.html", form=form, persons=persons)
   

@app.route('/home', methods=['POST','GET'])
def home():
    form = RegistrationForm()
    if request.method=='POST':
        print(form.email.data)
        print(form.comment.data)
        newentry=Course(email=form.email.data, comment=form.comment.data)
        db.session.add(newentry)
        db.session.commit()
        print("successful")
        return redirect("/home")
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
   
    
    return render_template("venue.html", form=form, persons=persons)

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
