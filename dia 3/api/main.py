from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/user')
def user():
  data = {'name': 'Alejandro', 'age': '25', 'email': 'alejandro@gmail.com'}
  print(type(data))
  print(type(jsonify(data)))
  return jsonify(data)


@app.route('/')
def home():
  return 'Hola'


app.run(host='0.0.0.0', debug=True)
