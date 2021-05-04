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
        datos = {
                'age': request.form['age'],
                'workclass': request.form['workclass'],
                'education': request.form['education'],
                'education-num': request.form['education-num'],
                'marital-status': request.form['marital-status'],
                'occupation': request.form['occupation'],
                'relationship': request.form['relationship'],
                'race': request.form['race'],
                'sex': request.form['sex'],
                'capital-gain': request.form['capital-gain'],
                'capital-loss': request.form['capital-loss'],
                'hours-per-week': request.form['hours-per-week'],
                'native-country': request.form['native-country'],
                'income': request.form['income']
                }
        print(datos)
        predictor = session.get('predictor', None)
        cosas = query.inout(datos,switcher[predictor])

        return render_template('end.html', datos=datos, cosas=cosas, predictor=predictor)

