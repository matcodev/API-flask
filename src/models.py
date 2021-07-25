from enum import unique
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'Usuarios'
    id = db.Column(db.Integer, primary_key=True)
    primerNombre = db.Column(db.String(255), nullable=False)
    segundoNombre = db.Column(db.String(255), nullable=True)
    apellidoPaterno = db.Column(db.String(255), nullable=False)
    apellidoMaterno = db.Column(db.String(255), nullable=True)
    fono = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(250), nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "primerNombre": self.primerNombre,
            "segundoNombre": self.segundoNombre,
            "apellidoPaterno": self.apellidoPaterno,
            "apellidoMaterno": self.apellidoMaterno,
            "fono": self.fono,
            "email": self.email,
            "contrasena": self.contrasena
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Clientes(db.Model):
    __tablename__ = 'Clientes'
    id = db.Column(db.Integer, primary_key=True)
    primerNombre = db.Column(db.String(255), nullable=False)
    segundoNombre = db.Column(db.String(255), nullable=True)
    apellidoPaterno = db.Column(db.String(255), nullable=False)
    apellidoMaterno = db.Column(db.String(255), nullable=True)
    fono = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(250), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "primerNombre": self.primerNombre,
            "segundoNombre": self.segundoNombre,
            "apellidoPaterno": self.apellidoPaterno,
            "apellidoMaterno": self.apellidoMaterno,
            "fono": self.fono,
            "email": self.email
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Servicios(db.Model):
    __tablename__ = 'Servicios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "valor": self.valor
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class EstadoReserva(db.Model):
    __tablename__ = 'EstadoReserva'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

# class UsuarioServicios(db.Model):
#     __tablename__ = 'UsuarioServicios'
#     estado = db.Column(db.String(50), nullable=False)

#     usuarioID = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable=False)
#     usuario = db.relationship('Usuarios', backref=db.backref('UsuarioServicios', lazy=True))

#     servicioID = db.Column(db.Integer, db.ForeignKey('Servicios.id'), nullable=False)
#     servicio = db.relationship('Servicios', backref=db.backref('UsuarioServicios', lazy=True))
    
UsuarioServicios = db.Table('UsuarioServicios', 
    db.Column('usuarioID', db.Integer, db.ForeignKey('Usuarios.id'), primary_key=True),
    db.Column('servicioID', db.Integer, db.ForeignKey('Servicios.id'), primary_key=True),
    db.Column('estado', db.Integer, nullable=False)
)

class Reserva(db.Model):
    __tablename__= 'Reserva'
    id = db.Column(db.Integer, primary_key=True)
    fechaReserva = db.Column(db.Date, nullable=False)
    horaReserva = db.Column(db.Time, nullable=False)

    servicioID = db.Column(db.Integer, db.ForeignKey('Servicios.id'), nullable=False)
    servicio = db.relationship('Servicios', backref=db.backref('Reserva', lazy=True))
    
    clienteID = db.Column(db.Integer, db.ForeignKey('Clientes.id'), nullable=False)
    cliente = db.relationship('Clientes', backref=db.backref('Reserva', lazy=True))
    
    estadoReservaID = db.Column(db.Integer, db.ForeignKey('EstadoReserva.id'), nullable=False)
    estadoReserva = db.relationship('EstadoReserva', backref=db.backref('Reserva', lazy=True))
    
    def serialize(self):
        return {
            "id": self.id,
            "servicioID": self.servicioID,
            "clienteID": self.clienteID,
            "fechaReserva": self.fechaReserva,
            "horaReserva": self.horaReserva,
            "estadoReservaID": self.estadoReservaID
        }
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()