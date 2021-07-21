from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token
from flask_cors import CORS
from models import User, db

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


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.json.get('username')
        password = request.json.get('password')

        user = User()
        user.username = username
        user.password = password
        user.save()

        access_token = create_access_token(identity=user.id)

        datos = {
            "access_token": access_token,
            "user": user.serialize()
        }

        return jsonify(datos), 201 

if __name__ == '__main__':
    app.run()