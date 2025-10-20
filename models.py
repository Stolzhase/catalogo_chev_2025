from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Coche(db.Model):
    """
    Modelo de datos para representar un coche en el catálogo
    """
    __tablename__ = 'coches'
    
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    año = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    color = db.Column(db.String(30), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_actualizacion = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, marca, modelo, año, precio, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.color = color
    
    def __repr__(self):
        return f'<Coche {self.marca} {self.modelo} ({self.año})>'
    
    def to_dict(self):
        """
        Convierte el objeto Coche a un diccionario para serialización JSON
        """
        return {
            'id': self.id,
            'marca': self.marca,
            'modelo': self.modelo,
            'año': self.año,
            'precio': self.precio,
            'color': self.color,
            'fecha_creacion': self.fecha_creacion.isoformat() if self.fecha_creacion else None,
            'fecha_actualizacion': self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None
        }
    
    @staticmethod
    def validar_año(año):
        """
        Valida que el año sea razonable
        """
        año_actual = datetime.now().year
        return 1900 <= año <= año_actual + 1
    
    @staticmethod
    def validar_precio(precio):
        """
        Valida que el precio sea positivo
        """
        return precio > 0
