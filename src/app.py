from os import access
from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS
from models import Usuarios, db, Clientes, Reserva, Servicios, UsuarioServicios, EstadoReserva

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = "development"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['JWT_SECRET_KEY'] = "secret-key"

db.init_app(app)
Migrate(app, db) #init, migrate, upgrade
jwt = JWTManager(app)
CORS(app)

@app.route("/login", methods=['POST'])
def create_token():
    email = request.json.get("email")
    contrasena = request.json.get("contrasena")

    user = Usuarios.query.filter(Usuarios.email == email, Usuarios.contrasena == contrasena).first()

    if user == None:
        return jsonify({
            "estado": "desactivado",
            "msg": "Error en email o contraseña"
        }), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token, usuarioID = user.id), 200

# obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
# @jwt_required()
def getUsuarios():
    user = Usuarios.query.all()
    user = list(map(lambda x: x.serialize(), user))
    return jsonify(user), 200

# obtener los usuarios por ID
@app.route('/usuarios/<id>', methods=['GET'])
def getUsuarioById(id):
    user = Usuarios.query.get(id)
    return jsonify(user.serialize()),200

@app.route('/usuarios/<id>', methods=['DELETE'])
def deleteUsuario(id):
    user = Usuarios.query.get(id)
    Usuarios.delete(user.id)
    return jsonify(user.serialize()),200

@app.route('/usuarios/<id>', methods=['PUT'])
def updateUsuario(id):
    user = Usuarios.query.get(id)

    user.primerNombre = request.json.get('primerNombre')
    user.segundoNombre = request.json.get('segundoNombre')
    user.apellidoPaterno = request.json.get('apellidoPaterno')
    user.apellidoMaterno = request.json.get('apellidoMaterno')
    user.fono = request.json.get('fono')
    user.email = request.json.get('email')
    user.contrasena = request.json.get('contrasena')
    
    Usuarios.update(user)

    return jsonify(user.serialize()),200

@app.route('/usuarios/', methods=['POST'])
def agregarUsuario():
    user = Usuarios()

    user.primerNombre = request.json.get('primerNombre')
    user.segundoNombre = request.json.get('segundoNombre')
    user.apellidoPaterno = request.json.get('apellidoPaterno')
    user.apellidoMaterno = request.json.get('apellidoMaterno')
    user.fono = request.json.get('fono')
    user.email = request.json.get('email')
    user.contrasena = request.json.get('contrasena')
    
    Usuarios.save(user)

    return jsonify(user.serialize()),200

# obtener todos los clientes

@app.route('/clientes', methods=['GET'])
def getClientes():
    clientes = Clientes.query.all()
    clientes = list(map(lambda x: x.serialize(), clientes))
    return jsonify(clientes), 200

@app.route('/clientes/<id>', methods=['GET'])
def getClienteById(id):
    cliente = Clientes.query.get(id)
    return jsonify(cliente.serialize()),200

@app.route('/clientes/<id>', methods=['DELETE'])
def deleteCliente(id):
    cliente = Usuarios.query.get(id)
    Usuarios.delete(cliente.id)
    return jsonify(cliente.serialize()),200

@app.route('/clientes/<id>', methods=['PUT'])
def updateCliente(id):
    cliente = Clientes.query.get(id)

    cliente.primerNombre = request.json.get('primerNombre')
    cliente.segundoNombre = request.json.get('segundoNombre')
    cliente.apellidoPaterno = request.json.get('apellidoPaterno')
    cliente.apellidoMaterno = request.json.get('apellidoMaterno')
    cliente.fono = request.json.get('fono')
    cliente.email = request.json.get('email')
    
    Usuarios.update(cliente)

    return jsonify(cliente.serialize()),200

@app.route('/clientes', methods=['POST'])
def agregarCliente():
    cliente = Clientes()

    cliente.primerNombre = request.json.get('primerNombre')
    cliente.segundoNombre = request.json.get('segundoNombre')
    cliente.apellidoPaterno = request.json.get('apellidoPaterno')
    cliente.apellidoMaterno = request.json.get('apellidoMaterno')
    cliente.fono = request.json.get('fono')
    cliente.email = request.json.get('email')
    
    Usuarios.save(cliente)

    return jsonify(cliente.serialize()),200





if __name__ == '__main__':
    app.run()