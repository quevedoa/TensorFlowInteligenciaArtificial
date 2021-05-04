from flask import Flask, render_template, request, send_file, url_for, redirect
import query

app = Flask(__name__)
@app.route('/', methods = ['POST', 'GET'])
def start():
    return render_template('index.html')

@app.route('/end', methods = ['POST'])
def end():
    if request.method == 'POST':
        datos = {
                'edad': request.form['edad'],
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
        cosas = query.inout(datos)

        return render_template('end.html', datos=datos, cosas=cosas)


