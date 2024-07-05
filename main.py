import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, SubmitField

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route ('/libros')
def libros():
    #Conectar con la base de datos#
    conexion = psycopg2.connect(
        database="biblioteca3a",
        user="postgres",
        password="k888"
        host="localhost"
        port="5432"
    )

    #crear un cursor (objeto para recorrer las tablas)
    cursor = conexion.cursor()
    #ejecutar una consulta en postgres
    cursor.execute('''SELECT * FROM libros''')
    #recuperar la informacion
    datos = cursor.fetchall()
    #cerrar cursor y conexion a la base de datos
    cursor.close()
    conexion.close()
    return render_template('libros.html', datos=datos)