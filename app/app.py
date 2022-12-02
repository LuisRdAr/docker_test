from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"


@app.route('/bbdd')
def bbdd():
    user = "schedulin"
    passw = "schedulin01"
    host = "35.227.3.172"
    database = "schedulin"

    db = create_engine(
    'mysql+pymysql://{0}:{1}@{2}/{3}' \
        .format(user, passw, host, database), \
    connect_args = {'connect_timeout': 10})
    
    conn = db.connect()

    select = "SHOW TABLES;"

    result = conn.execute(timetable_creation).fetchall()

    print("Estás conectado a la BBDD de schedulin! \
        \nEstas son las tablas que contiene: \n{}".format(result))

    return

app.run()