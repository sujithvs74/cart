from flask import Flask, jsonify, request, Response
import json
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('config.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

def validCartItem(item):
    if("name" in item and "price" in item and "id" in item):
        return True
    else:
        return False

@app.route('/add_cart', methods=['POST'])
def add_item():
    request_data = request.get_json()
    if(validCartItem(request_data)):
        name = request_data['name']
        price = request_data['price']
        id = request_data['id']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO items(name, price, id) VALUES(%s, %s, %s)",(name, int(price), int(id)))
        mysql.connection.commit()
        cur.close()
        response = Response("", 201, mimetype='application/json')
        return "Item added to cart!"
    else:
        invalidCartItemErrorMsg = {
            "error": "Invalid cart object passed in request",
            "helpString": "Data passed in similar to this {'name': 'xyz', 'price': 34, 'id': 1234}"
        }
        response = Response(json.dumps(invalidCartItemErrorMsg), status=400, mimetype='application/json')
        return response

@app.route('/view_cart')
def get_items():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM items")
    if resultValue > 0:
        cartDetails = cur.fetchall()
    return jsonify(cartDetails)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)