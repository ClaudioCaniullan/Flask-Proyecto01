from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash, get_flashed_messages
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest


# crear instancias
app = Flask(__name__)
app.config.update(DEBUG=True, ENV='development')
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'super secreto'

todo = ['comprar te chino', 'enviar solicitud de compra', 'entrega de productos']


class LoginForm(FlaskForm):
    username = StringField('nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('enviar') # no necesita un validador


@app.cli.command()
def test():
    test = unittest.TestLoader.discover('tests')
    unittest.TextTestRunner.run(tests)

# manejo del error 404
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
    
    

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    #response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    
    return response


# enrutador con su respectiva función 
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = { 'user_ip': user_ip, 
               'todo': todo,
               'login_form': login_form,
               'username': username}
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        
        flash('Nombre de usuario registrado con exito')
        
        return redirect(url_for('index'))
    
    return render_template('hello.html', **context)



# Desde la terminal ejecutar: python main.py
if __name__ == '__main__':
    app.run(port = 5000)