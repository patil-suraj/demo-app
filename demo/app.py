from flask import Flask
from flask_mysql_connector import MySQL

app = Flask(__name__)


app = Flask(__name__)
app.config['MYSQL_USER'] = "vckonline"
app.config['MYSQL_DATABASE'] = "demo"
app.config["MYSQL_PASSWORD"] = "sumBuOUDZ9UlQgkf1qrU"
mysql = MySQL(app)

EXAMPLE_SQL = 'select * from demo.pet'


@app.route('/')
def hello_world():
    # conn = mysql.connection
    # cur = conn.cursor()
    # cur.execute(EXAMPLE_SQL)
    # output = cur.fetchall()
    # return str(output)
    return 'Hello, World!'


# if __name__ == "__main__":
    # app.run(host='0.0.0.0', port='8080', debug=True)
