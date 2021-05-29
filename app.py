from logging import PlaceHolder, error
from flask import Flask, render_template, request, url_for, jsonify
from werkzeug.exceptions import HTTPException, abort
from gethero import get_super_byName
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretKey'

class HeroForm(FlaskForm):
    # clase para representar el formulario, viene la libreria WTF
    name = StringField('Hero: ', validators=[DataRequired()]) # hero es el label del form
    

@app.errorhandler(404)
def page_not_found(error):
    # manejador de ruta de error
    return render_template('page_not_found.html'), 404

@app.route('/')
def index():  
    form = HeroForm()  
    data = get_super_byName('spider-man') # obtiene la data del heroe o villano
    power_stats = [power for power in data.get('powerstats').values()]
    context = [[key, val] for (key, val) in data.get('powerstats').items()] #obtiene la lista de poderes
    
    return render_template('search.html', form = form, data = data, power = power_stats, context=context)

@app.post('/') # decorador usado desde Flask 2.0 en adicin a methods=['GET', 'POST']
def homePost():
    try:
        form = HeroForm()
        if form.validate_on_submit(): # validador del formulario
            data = get_super_byName(form.name.data)            
            context = [[key, val] for (key, val) in data.get('powerstats').items()]
            
            return render_template('search.html', form = form, data = data, context=context)
    except Exception:
        return abort(404) #render_template('page_not_found.html')
    

@app.route('/hello', methods=['GET', 'POST']) 
# metodo para probar la comunicación de Javascript con Flask (no usado en la app)
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON
        return 'OK', 200

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

if __name__ == '__main__':
    #set FLASK_ENV=development  -- Permite cambiar a ambiente de desarrollo cuando DEBUG no se ejecuta
    app.run(host='192.168.0.99', port = 5000, threaded=True, debug=True)