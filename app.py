from flask import Flask, render_template, request, send_file, url_for, redirect, session
import query


app = Flask(__name__)

app.secret_key = 'arturo'

switcher = {
    "Age":0,
    "Workclass":1,
    "Education":2,
    "Education Num":3,
    "Marital Status":4,
    "Occupation":5,
    "Relationship":6,
    "Race":7,
    "Sex":8,
    "Capital Gain":9,
    "Capital Loss":10,
    "Hours per Week":11,
    "Native Country":12,
    "Income (=&lt50k or &gt50k)":13
}

@app.route('/', methods = ['POST', 'GET'])
def start():
    return render_template('index.html')

@app.route('/fill', methods = ['POST', 'GET'])
def fill():
    if request.method == 'POST':
        predictor = request.form['predictor']
        session['predictor'] = predictor

    return render_template('fill.html', predictor = switcher[predictor], pred = predictor)

@app.route('/end', methods = ['POST', 'GET'])
def end():
    if request.method == 'POST':
        predictor = session.get('predictor', None)

        datos = {}
        outer = switcher[predictor]
        i=0

        if i != outer:
            datos['age']=request.form['age']
        i+=1
        if i != outer:
            datos['workclass']=request.form['workclass']
        i+=1
        if i != outer:
            datos['education']=request.form['education']
        i+=1
        if i != outer:
            datos['education-num']=request.form['education-num']
        i+=1
        if i != outer:
            datos['marital-status']=request.form['marital-status']
        i+=1
        if i != outer:
            datos['occupation']=request.form['occupation']
        i+=1
        if i != outer:
            datos['relationship']=request.form['relationship']
        i+=1
        if i != outer:
            datos['race']=request.form['race']
        i+=1
        if i != outer:
            datos['sex']=request.form['sex']
        i+=1
        if i != outer:
            datos['capital-gain']=request.form['capital-gain']
        i+=1
        if i != outer:
            datos['capital-loss']=request.form['capital-loss']
        i+=1
        if i != outer:
            datos['hours-per-week']=request.form['hours-per-week']
        i+=1
        if i != outer:
            datos['native-country']=request.form['native-country']
        i+=1
        if i != outer:
            datos['income']=request.form['income']
        
        print(datos)
        
        cosas = query.inout(datos,switcher[predictor])

        return render_template('end.html', datos=datos, cosas=cosas, predictor=predictor)

