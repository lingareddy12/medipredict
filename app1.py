from flask import Flask, render_template, url_for,session
from flask_wtf import FlaskForm
from wtforms import  FloatField, SubmitField,RadioField,SelectField,StringField
from wtforms.validators import InputRequired, NumberRange,ValidationError,Length
from flask_bootstrap import Bootstrap
import pandas as pd
from  joblib import load

import mysql.connector



loaded_breast = load('mysite/weights/breast_reg.joblib')
class breastcancer:
    def predict(self,val):
        df=pd.DataFrame(columns=['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
       'perimeter_se', 'area_se', 'radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst'])
        df.loc[len(df)] = val
        y_pred = loaded_breast.predict_proba(df[:1])[:, 1]
        return y_pred[0]

loaded_heart = load('mysite/weights/heart_svm.joblib')
class heart:
    def predict(self,val):
        df1=pd.DataFrame(columns=['age', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke','active'])
        df1.loc[len(df1)] = val
        y_pred = loaded_heart.predict_proba(df1[:1])[:, 1]
        return y_pred[0]

loaded_diabetic = load('mysite/weights/diabetes_reg.joblib')
class diabetes:
    def predict_val(self,val):
        df1=pd.DataFrame(columns=['Pregnancies', 'Glucose', 'BloodPressure', 'Insulin', 'BMI',
       'DiabetesPedigreeFunction', 'Age'])
        df1.loc[len(df1)] = val
        y_pred = loaded_diabetic.predict_proba(df1[:1])[:, 1]
        return y_pred[0]


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
Bootstrap(app)

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(min=4, max=20)])
    dis = SelectField('Disease Type', choices=[('Breast Cancer'),('Diabetes'),('CardioVascular')])
    review = SelectField('Is Our Prediction Accurate', choices=[('yes'),('no')])
    submit=SubmitField("Submit")

class heartform(FlaskForm):
    age = FloatField('Age', validators=[InputRequired(),NumberRange(min=0, max=125)])
    weight= FloatField('Weight', validators=[InputRequired(),NumberRange(min=0, max=200)])
    ap_hi= FloatField('Systolic blood pressure ', validators=[InputRequired(),NumberRange(min=0, max=200)])
    ap_lo= FloatField('Diastolic blood pressure ', validators=[InputRequired(),NumberRange(min=0, max=200)])
    chol = SelectField('cholestrol level', choices=[('normal'),('above normal'),('Well above normal')])
    gluc = SelectField('Glucose level', choices=[('normal'),('above normal'),('Well above normal')])
    alco= RadioField('Smoke',choices=[('yes'),('no')] ,validators=[InputRequired()])
    active= RadioField('Active',choices=[('yes'),('no')], validators=[InputRequired()])
    submit=SubmitField("submit")
    def validate_my_float(self, field):
        if field.data is not None and not isinstance(field.data, float):
            raise ValidationError ("Invalid input. Please enter a float value")

class diabeteform(FlaskForm):
    preg = FloatField('Pregnancies', validators=[InputRequired(),NumberRange(min=0, max=20)])
    gluc= FloatField('Glucose', validators=[InputRequired(),NumberRange(min=0, max=300)])
    bp= FloatField('Blood Pressure ', validators=[InputRequired(),NumberRange(min=0, max=200)])
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
        return "Patient has low risk "
    elif(0.3<=val<=0.7):
        return "Patient has moderate risk"
    else:
        return "Patient has high risk "

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
            chol=1
            print("normal")
        elif chol=="above normal":
            chol=2
        else:
            chol=3

        gluc=form.gluc.data

        if gluc=='normal':
            gluc=1
        elif gluc=='above normal':
            gluc=2
        else:
            gluc=3

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
        heart_val=a.predict([age,weight,ap_hi,ap_lo,chol,gluc,alco,active])
        session['heart_values']=[age,weight,ap_hi,ap_lo,chol,gluc,alco,active,heart_val]
        url="https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118"
        return render_template("result.html",result=result(heart_val),disease="CardioVascular Disease",url=url,val=heart_val)

    return render_template('heart.html', form=form)

@app.route('/diabetes', methods=['GET','POST'])
def diabetes_pred():
    form = diabeteform()
    if form.validate_on_submit():
        preg = form.preg.data
        gluc= form.gluc.data
        bp= form.bp.data
        ins = form.ins.data
        bmi= form.bmi.data
        dpf= form.dpf.data
        age = form.age.data
        a=diabetes()
        diabet_val=a.predict_val([preg,gluc,bp,ins,bmi,dpf,age])
        session['diabet_values']=[preg,gluc,bp,ins,bmi,dpf,age,diabet_val]
        url="https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444"
        return render_template("result.html",result=result(diabet_val),disease="Diabetes",url=url,val=diabet_val)


    return render_template('diabete.html', form=form)

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
        breast_val=a.predict([r_m,t_m,p_m,a_m,p_s,a_s,r_w,t_w,p_w,a_w])
        session['breast_values']=[r_m,t_m,p_m,a_m,p_s,a_s,r_w,t_w,p_w,a_w,breast_val]
        if breast_val<=0.2:
            disease="Benign"
            breast_val=1-breast_val
        elif 0.2<breast_val<=0.45:
            breast_val=1-breast_val
            disease="Benign"
        elif 0.45<breast_val<=0.49999:
            breast_val=0.5-breast_val
            disease="Benign"
        elif 0.49999<breast_val<=0.6:
            breast_val=breast_val-0.49999
            disease="Malignant"
        else:
            disease="Malignant"



        url="https://www.mayoclinic.org/diseases-conditions/breast-cancer/symptoms-causes/syc-20352470"
        return render_template("result.html",result=result(breast_val),disease=disease,url=url,val=breast_val)
    return render_template("breast.html",form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        dis=form.dis.data
        review=form.review.data
        if review=='yes':
            review=1
        else:
            review=0

        if dis=="Diabetes":
            diabet_val=int(round(session.get('diabet_values')[-1]))
            if review!=1:
                diabet_val=diabet_val^1
            session.get('diabet_values')[-1]=diabet_val
            val= session.get('diabet_values')
            mydb=mysql.connector.connect(host='Medi2Predict.mysql.pythonanywhere-services.com',user='Medi2Predict',password='Linga@12#',database="Medi2Predict$MediPredict")
            mycursor = mydb.cursor()
            insert_query = """
                    INSERT INTO diabetes (name ,preg, gluc, bp, ins, bmi, dpf, age, diabet_val)
                    VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s) """
            data = (name,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7])
            mycursor.execute(insert_query, data)
            mydb.commit()
            mycursor.close()
            mydb.close()
        elif dis=="Breast Cancer":
            breast_val=int(round(session.get('breast_values')[-1]))
            if review!=1:
                breast_val=breast_val^1
            session.get('breast_values')[-1]=breast_val
            val= session.get('breast_values')
            mydb=mysql.connector.connect(host='Medi2Predict.mysql.pythonanywhere-services.com',user='Medi2Predict',password='Linga@12#',database="Medi2Predict$MediPredict")
            mycursor = mydb.cursor()
            insert_query = """
                        INSERT INTO breastcancer (name, radius_mean, texture_mean, perimeter_mean,
                        area_mean, perimeter_se, area_se, radius_worst, texture_worst, perimeter_worst, area_worst, breast_val)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            data = (name,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8],val[9],val[10])
            mycursor.execute(insert_query, data)
            mydb.commit()
            mycursor.close()
            mydb.close()
        else:
            heart_val=int(round(session.get('heart_values')[-1]))
            if review!=1:
                heart_val=heart_val^1
            session.get('heart_values')[-1]=heart_val
            val= session.get('heart_values')
            mydb=mysql.connector.connect(host='Medi2Predict.mysql.pythonanywhere-services.com',user='Medi2Predict',password='Linga@12#',database="Medi2Predict$MediPredict")
            mycursor = mydb.cursor()
            insert_query = """
                           INSERT INTO heart (name,age, weight, bp_hi, bp_lo, chol, gluc, alco, active,result)
                           VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s,%s)
                              """
            data = (name,val[0],val[1],val[2],val[3],val[4],val[5],val[6],val[7],val[8])
            mycursor.execute(insert_query, data)
            mydb.commit()
            mycursor.close()
            mydb.close()



        return render_template('thankyou.html')
    return render_template('signup.html',form=form)





if __name__ == '__main__':
    app.run(debug=True)
