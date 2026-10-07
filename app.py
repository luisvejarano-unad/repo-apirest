from flask import Flask, jsonify

app = Flask(__name__)

# Lista de estudiantes
estudiantes = [
    {
        "id": 1,
        "nombre": "Ana García",
        "programa": "Ingeniería de Sistemas"
    },
    {
        "id": 2,
        "nombre": "Carlos Rodríguez",
        "programa": "Ingeniería de Software"
    },
    {
        "id": 3,
        "nombre": "María López",
        "programa": "Ingeniería de Sistemas"
    }
]


# GET - Listar todos los estudiantes
@app.route("/api/estudiantes", methods=["GET"])
def listar_estudiantes():
    return jsonify(estudiantes)


# GET - Buscar estudiante por ID
@app.route("/api/estudiantes/<int:id>", methods=["GET"])
def buscar_estudiante(id):

    for estudiante in estudiantes:
        if estudiante["id"] == id:
            return jsonify(estudiante)

    return jsonify({
        "mensaje": "Estudiante no encontrado"
    }), 404


# Iniciar servidor
if __name__ == "__main__":
    app.run(debug=True)
