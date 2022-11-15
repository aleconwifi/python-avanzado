from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route('/pagina2')
def pagina2():
  return "<h2 style='color:pink'> Esta es la pagina 2 </h2>"

@app.route('/curso/alumnos')
def get_alumnos():
  alumnos = ['Ricardo', 'Rafael', 'Fernando']
  data = {'pagetitle': 'Titulo Alumnos', 'nombres': alumnos}
  return render_template('lista_alumnos.html', data=data)

@app.route("/curso/alumno/<id>")
def get_alumno(id):
  return "Esta es la info del Estudiante" + id

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
