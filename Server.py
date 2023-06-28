from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField,RadioField,PasswordField,SelectField
from wtforms.validators import InputRequired, NumberRange,ValidationError
from heart_predict import heart
from diabetes_predict import diabetes
from breast_cancer import breastcancer
from flask_bootstrap import Bootstrap
import numpy as np


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
Bootstrap(app) 

        
        
class heartform(FlaskForm):
    age = FloatField('Age', validators=[InputRequired(),NumberRange(min=0, max=125)])
    weight= FloatField('Weight', validators=[InputRequired(),NumberRange(min=0, max=200)])
    ap_hi= FloatField('Systolic blood pressure ', validators=[InputRequired(),NumberRange(min=0, max=200)])
    ap_lo= FloatField('Diastolic blood pressure ', validators=[InputRequired(),NumberRange(min=0, max=200)])
    chol = SelectField('cholestrol level', choices=[('normal'),('Well above normal')])
    gluc = SelectField('Glucose level', choices=[('normal'),('Well above normal')])
    alco= RadioField('Alcohol',choices=[('yes'),('no')] ,validators=[InputRequired()])
    active= RadioField('Active',choices=[('yes'),('no')], validators=[InputRequired()])
    submit=SubmitField("submit")
    def validate_my_float(self, field):
        if field.data is not None and not isinstance(field.data, float):
            raise ValidationError ("Invalid input. Please enter a float value")

class diabeteform(FlaskForm):
    preg = FloatField('Pregnancies', validators=[InputRequired(),NumberRange(min=0, max=20)])
    gluc= FloatField('Glucose', validators=[InputRequired(),NumberRange(min=0, max=300)])
    bp= FloatField('Blood Pressure ', validators=[InputRequired(),NumberRange(min=0, max=200)])
    skin= FloatField('Skin Thickness', validators=[InputRequired(),NumberRange(min=0, max=200)])
    ins = FloatField('Insulin', validators=[InputRequired(),NumberRange(min=0, max=120)])
    bmi= FloatField('BMI', validators=[InputRequired(),NumberRange(min=0, max=800)])
    dpf= FloatField('Diabetic Pedigree Function', validators=[InputRequired(),NumberRange(min=0, max=10)])
    age= FloatField('Age', validators=[InputRequired(),NumberRange(min=0, max=150)])
    submit=SubmitField("submit")
    def validate_my_float(self, field):
        if field.data is not None and not isinstance(field.data, float):
            raise ValidationError ("Invalid input. Please enter a float value")
    
class breastcancerform(FlaskForm):
    r_m = FloatField('Radius_mean', validators=[InputRequired(),NumberRange(min=0, max=200)])
    t_m= FloatField('Texture_mean', validators=[InputRequired(),NumberRange(min=0, max=300)])
    p_m= FloatField('Perimeter_mean', validators=[InputRequired(),NumberRange(min=0, max=200)])
    a_m= FloatField('Area_mean', validators=[InputRequired(),NumberRange(min=0, max=2000)])
    p_s= FloatField('Perimeter_se', validators=[InputRequired(),NumberRange(min=0, max=1000)])
    a_s= FloatField('Area_se', validators=[InputRequired(),NumberRange(min=0, max=800)])
    r_w= FloatField('Radius_worst', validators=[InputRequired(),NumberRange(min=0, max=1000)])
    t_w= FloatField('Texture_worst', validators=[InputRequired(),NumberRange(min=0, max=1500)])
    p_w= FloatField('Perimeter_worst', validators=[InputRequired(),NumberRange(min=0, max=1000)])
    a_w= FloatField('Area_worst', validators=[InputRequired(),NumberRange(min=0, max=1000)])
    submit=SubmitField("submit")
    def validate_my_float(self, field):
        if field.data is not None and not isinstance(field.data, float):
            raise ValidationError ("Invalid input. Please enter a float value")

def result(val):
    if(val<0.3):
        return f"Patient has low risk "
    elif(0.3<=val<=0.7):
        return f"Patient has moderate risk"
    else:
        return f"Patient has high risk "
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def diseases():
    return render_template("diseases.html")

@app.route('/heart', methods=['GET','POST'])
def heart_pred():
    form = heartform()
    if form.validate_on_submit():
        
        age=form.age.data
        weight=form.weight.data
        ap_hi=form.ap_hi.data
        ap_lo=form.ap_lo.data
        
        chol=form.chol.data 
        if chol=='normal':
            chol=0
        else:
            chol=1
            
        gluc=form.gluc.data 
        if gluc=='normal':
            gluc=1
        else:
            gluc=0
            
        alco=form.alco.data
        if alco=="no":
            alco=0
        else:
            alco=1 
            
        active=form.active.data 
        if active=="no":
            active=0
        else:
            active=1 
            
        a=heart()
        val=a.predict([age*0.0188,weight/274,ap_hi/127,ap_lo/82,chol,gluc,alco,active]) 
        url="https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118"
        return render_template("result.html",result=result(val),disease="CardioVascular Disease",url=url,val=val)

    return render_template('heart.html', form=form)

@app.route('/diabetes', methods=['GET','POST'])
def diabetes_pred():
    form = diabeteform()
    if form.validate_on_submit():
        preg = form.preg.data 
        gluc= form.gluc.data
        bp= form.bp.data
        skin = form.skin.data
        ins = form.ins.data 
        bmi= form.bmi.data
        dpf= form.dpf.data
        age = form.age.data
        a=diabetes()
        val=a.predict_val([preg/17,gluc/199,bp/122,skin/99,ins/846,bmi/67.1,dpf/2.42,age/81])
        url="https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444"
        return render_template("result.html",result=result(val),disease="Diabetes",url=url,val=val)
        

    return render_template('diabetes.html', form=form)

@app.route('/breastcancer', methods=['GET','POST'])
def breastcancer_pred():
    form = breastcancerform()
    if form.validate_on_submit():
        r_m = form.r_m.data 
        t_m= form.t_m.data
        p_m= form.p_m.data
        a_m = form.a_m.data
        p_s= form.p_s.data 
        a_s= form.a_s.data
        r_w= form.r_w.data
        t_w= form.t_w.data
        p_w= form.p_w.data
        a_w= form.a_w.data
        a=breastcancer()
        val=a.predict([r_m,t_m,p_m,a_m,p_s,a_s,r_w,t_w,p_w,a_w]) 
        if val==1:
            disease="malignant"
        else:
            disease="benign"
            val=1
        url="https://www.mayoclinic.org/diseases-conditions/breast-cancer/symptoms-causes/syc-20352470"
        return render_template("result.html",result=result(val),disease=disease,url=url)
    return render_template("breast.html",form=form)





if __name__ == '__main__':
    app.run(debug=True)
