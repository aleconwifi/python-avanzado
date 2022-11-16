from flask import Flask, request, abort, make_response, jsonify

tasks = [
    {
        "id": 1,
        "title": u"Buy groceries",
        "description": u"Milk, Cheese, Pizza, Fruit, Tylenol",
        "done": False,
    },
    {
        "id": 2,
        "title": u"Learn Python",
        "description": u"Need to find a good Python tutorial on the web",
        "done": True,
    },
]

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route("/")
def hola():
    return "Bienvenido a Flask"

def _new(title, desc):

    nueva_tarea = {
        "id": int(tasks[-1]["id"]) + 1,
        "title": title,
        "description": desc,
        "done": False,
    }

    tasks.append(nueva_tarea)

    return nueva_tarea


@app.route("/tareas", methods=["GET", "POST"])
def get_tareas():
    if request.method =="GET":
        return jsonify({'tareas': tasks})
    else:
        nueva_tarea = _new(
          title=request.json["title"], desc=request.json["description"]
        )
        return jsonify({"tarea": nueva_tarea}), 201



@app.route("/tareas/<int:id_tarea>", methods=["GET"])
def get_taks(id_tarea):

    tarea = None

    for t in tasks:
        if t["id"] == id_tarea:
            tarea = t
            break

    if not tarea:
        abort(404)

    return jsonify({"tarea": tarea})


app.run(host="0.0.0.0", port=3000, debug=True)