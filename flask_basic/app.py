from logging import debug
from os import read
from flask import Flask,render_template,request,session,flash
import flask
from flask_wtf import FlaskForm
from flask_wtf.form import _is_submitted
from wtforms import TextField,SubmitField,BooleanField,RadioField,SelectField,TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)


class MyForm(FlaskForm):
    name = TextField("ป้อนชื่อของคุณ",validators=[DataRequired()])
    address = TextAreaField('ป้อนที่อยู่ของคุณ',validators=[DataRequired()])
    isAccept = BooleanField("ยอมรับเงื่อนไข",validators=[DataRequired()])
    gender = RadioField('gender',choices=[('male','ชาย'),('Female','หญิง'),('trans','อื่นๆ')],validators=[DataRequired()])
    skill = SelectField('ความสามารถ',choices=[('Python','Python'),('C++','C++'),('CSS/HTML','CSS/HTML'),('Java','Java')],validators=[DataRequired()])
    submit = SubmitField("บันทึกข้อมูล",validators=[DataRequired()])



@app.route('/',methods=['get','post'])
def index():

    # name = False
    # form = MyForm()
    # isAccept= False
    # gender = False
    # skill = False
    # address = False
    form = MyForm()
    if form.validate_on_submit():

        session['name']= form.name.data
        session['isAccept']= form.isAccept.data
        session['gender']= form.gender.data
        session['skill'] = form.skill.data
        session['address']= form.address.data
        # clearData
        form.name.data =  ""
        form.isAccept.data =  ""
        form.gender.data =  ""
        form.skill.data =  ""
        form.address.data = ""


    # data = {"name":"Bot02","age":"22","salary":"150000"}
    # return render_template("index.html",form = form,name=name,isAccept=isAccept,gender=gender,skill=skill,address=address)
    return render_template("index.html",form=form)



@app.route('/boostarp',methods=['get','post'])
def index_boostrap():

    # name = False
    # form = MyForm()
    # isAccept= False
    # gender = False
    # skill = False
    # address = False
    form = MyForm()
    if form.validate_on_submit():

        flash("บันทึกข้อมูลเรียบร้อย")

        session['name']= form.name.data
        session['isAccept']= form.isAccept.data
        session['gender']= form.gender.data
        session['skill'] = form.skill.data
        session['address']= form.address.data
        # clearData
        form.name.data =  ""
        form.isAccept.data =  ""
        form.gender.data =  ""
        form.skill.data =  ""
        form.address.data = ""


    # data = {"name":"Bot02","age":"22","salary":"150000"}
    # return render_template("index.html",form = form,name=name,isAccept=isAccept,gender=gender,skill=skill,address=address)
    return render_template("index_boostrap.html",form=form)

@app.route('/about')
def about():
    product = ["เสื้อผ้า","เตารีด","ผ้าห่ม","ยาสามัญ"]
    return render_template("about.html",Myproduct = product)

@app.route('/admin')
def admin():
    #ชื่อ อายุ
    name = "bot01"
    age = 30
    return render_template("admin.html",Myname = name,Myage = age)

@app.route('/seddata')
def sigupfrom():
    fname=request.args.get('fname')
    descriptio = request.args.get('description')
    return render_template('thankyou.html',data={"name":fname,"description":descriptio})

# @app.route('/user/<name>/<age>')
# def member(name,age):
#     return "Hello member : {} , age : {}".format(name,age)

if __name__ == "__main__":
    app.run(debug=True)