
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, render_template, url_for,request,flash
import urllib.request, urllib.parse
from forms import *
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SECRET_KEY']= 'ADKADKFJ'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
migrate= Migrate(app, db)


def sendtelegram(params):
    url = "https://api.telegram.org/bot5787281305:AAE1S8DSnMAyQuzAnXOHfxLq-iyvPwYJeAo/sendMessage?chat_id=-1001556929308&text=" + urllib.parse.quote(params)
    content = urllib.request.urlopen(url).read()
    print(content)
    return content

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=True, unique=True)
    comment = db.Column(db.String(), nullable=True)
    budget =db.Column(db.String())
    def __repr__(self):
        return f"Course('{self.id}', {self.email}', {self.comment}')"

class Src(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    srcname = db.Column(db.String())
    name = db.Column(db.String())
    srcnumb= db.Column(db.String())
    Hoodie =db.Column(db.String())
    sweat =db.Column(db.String())
    bag =db.Column(db.String())
    shirt =db.Column(db.String())
    
    def __repr__(self):
        return f"Course('{self.id}', {self.number}', {self.name}')"

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    def __repr__(self):
        return f"Course('{self.id}', {self.name}')"

class Central(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String())
    def __repr__(self):
        return f"Course('{self.id}', {self.phone}')"
    
    
    
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
    form = SRCC()
    if request.method=='POST':
        
       
        print(form.name.data)
        print(form.srcname.data)
        print(form.sweat.data)
        print(form.srcnumb.data)
       
        src=Src(srcname=form.srcname.data,
sweat=form.data,
                srcnumb=form.srcnumb.data,
                name=form.name.data,
                
               
              )
        db.session.add(src)
        db.session.commit()
        print(src.sweat)
        
        print(src.srcnumb)
        print(src.srcname)
        
        
        print(src.name)
        sendtelegram("REQUEST ITEM" + '\n' + 
                      "Name = " + src.srcname  + '\n' + 
                      "Number = " + src.srcnumb  + '\n' + 
                      "Item = " + src.name
        )
        flash("We will call you in a minute, search ID:CM0111#.","success")
        return redirect("/about")
    return render_template('about.html')




@app.route('/shop',methods=['GET','POST'])
def shop():
    form = SRCC()
    if request.method=='POST':
        print(form.sweat.data)
        print(form.shirt.data)
        print(form.name.data)
        print(form.srcname.data)
        print(form.Hoodie.data)
        print(form.srcnumb.data)
        print(form.bag.data)
        src=Src(srcname=form.srcname.data,
                shirt=form.shirt.data,
                srcnumb=form.srcnumb.data,
                name=form.name.data,
                Hoodie=form.Hoodie.data,
                sweat=form.sweat.data,
              bag=form.bag.data)
        db.session.add(src)
        db.session.commit()
        print(src.sweat)
        print(src.shirt)
        print(src.srcnumb)
        print(src.srcname)
        print(src.Hoodie)
        print(src.sweat)
        print(src.name)
        sendtelegram("SRC POP-UP STORE ORDER:" + '\n' + 
                      "Name = " + src.srcname  + '\n' + 
                      "Number = " + src.srcnumb  + '\n' + 
                      "Hostel = " + src.name  + '\n' + 
                      "Qty Hoodie = " + src.Hoodie  + '\n' + 
                      "Qty Bag = " + src.bag  + '\n' + 
                    "Qty Shirt = " + src.shirt  + '\n' + 
                    "Qty Sweat Shirt = " + src.sweat)
        flash("Order Confirmed, Delivery is in the next 5 minutes","success")
        return redirect("/centralmal")
    persons=Src.query.order_by(Src.id.desc()).all()
    print(persons)
    return render_template('shop.html',persons=persons)

@app.route('/centralmal',methods=['GET','POST'])
def centralmal():
    form = SRCC()
    if request.method=='POST':
        
       
        print(form.name.data)
        print(form.srcname.data)
       
        print(form.srcnumb.data)
       
        src=Src(srcname=form.srcname.data,
                
                srcnumb=form.srcnumb.data,
                name=form.name.data,
                
               
              )
        db.session.add(src)
        db.session.commit()
      
        print(src.srcnumb)
        print(src.srcname)
        print(src.name)
        sendtelegram("REQUEST ITEM" + '\n' + 
                      "Name = " + src.srcname  + '\n' + 
                      "Number = " + src.srcnumb  + '\n' + 
                      "Item = " + src.name  
                   
        )
        flash("We are currently restocking, Our team will call you in a minute.","success")
        return redirect("/centralmal")
    return render_template('centralmal.html')


@app.route('/kalitexcreatives',methods=['GET','POST'])
def kalitexcreatives():
    
    return render_template('kalitexcreativs.html')



@app.route('/trail')
def trial():
    
    return render_template('trail.html')

@app.route('/lydia',methods=['GET','POST'])
def lydia():
    form = SRCC()
    if request.method=='POST':
        print(form.sweat.data)
       
        print(form.name.data)
        print(form.srcname.data)
       
        print(form.srcnumb.data)
       
        src=Src(srcname=form.srcname.data,
                
                srcnumb=form.srcnumb.data,
                name=form.name.data,
                
                sweat=form.sweat.data,
              )
        db.session.add(src)
        db.session.commit()
        print(src.sweat)
        
        print(src.srcnumb)
        print(src.srcname)
        
        
        print(src.name)
        sendtelegram("LYNAF CENTRAL ORDER:" + '\n' + 
                      "Name = " + src.srcname  + '\n' + 
                      "Number = " + src.srcnumb  + '\n' + 
                      "Hostel = " + src.name  + '\n' + 
                    "Quantity Bodycon= " + src.sweat)
        flash("We will call you in a minute to confirm your order, Preoder ID:CM2840201#.","success")
        return redirect("/centralmal")
    return render_template('lydia.html')


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

@app.route('/review')
def review():
    
    return render_template('happy.html')

@app.route('/search',methods=['GET','POST'])
def search():
    form = SRCC()
    if request.method=='POST':
        
       
        print(form.name.data)
        print(form.srcname.data)
       
        print(form.srcnumb.data)
       
        src=Src(srcname=form.srcname.data,
                
                srcnumb=form.srcnumb.data,
                name=form.name.data,
                
               
              )
        db.session.add(src)
        db.session.commit()
        print(src.sweat)
        
        print(src.srcnumb)
        print(src.srcname)
        
        
        print(src.name)
        sendtelegram("REQUEST ITEM" + '\n' + 
                      "Name = " + src.srcname  + '\n' + 
                      "Number = " + src.srcnumb  + '\n' + 
                      "Item = " + src.name
        )
        flash("We will call you in a minute, search ID:CM0111#.","success")
        return redirect("/search")
    return render_template('search.html')

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
    form = First()
    if request.method=='POST':
        print(form.name.data)
        
     
        newentry=Item(name=form.name.data)
        db.session.add(newentry)
        db.session.commit()
        print("successful")
        return redirect("/home")
    persons=Course.query.order_by(Course.id.desc()).all()
    print(persons)
    
    
    return render_template("index2.html", form=form, persons=persons)



@app.route('/additem')
def additem():
    return render_template("additem.html")


@app.route('/form')
def form():
    return render_template("form.html")
  
@app.route('/welcome' , methods=['POST', 'GET'])
def welcome():
    form = First()
    if request.method=='POST':
        print(form.name.data)
     
        newentry=Item(name=form.name.data)
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
