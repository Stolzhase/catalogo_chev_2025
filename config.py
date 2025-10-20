import os

class Config:
    """
    Configuración de la aplicación Flask
    """
    # Clave secreta para sesiones (cambiar en producción)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-desarrollo-2025'
    
    # Configuración de la base de datos SQLite
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///catalogo_coches.db'
    
    # Desactivar el seguimiento de modificaciones de SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configuración JSON
    JSON_AS_ASCII = False  # Para soportar caracteres especiales en español
    JSONIFY_PRETTYPRINT_REGULAR = True
