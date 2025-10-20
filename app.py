from flask import Flask, jsonify, request
from flask_cors import CORS
from models import Coche, db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos
db.init_app(app)

# Habilitar CORS para permitir peticiones desde el frontend
CORS(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

# Ruta principal
@app.route('/')
def index():
    return jsonify({
        'mensaje': 'API de Catálogo de Coches',
        'version': '1.0',
        'endpoints': {
            'GET /api/coches': 'Obtener todos los coches',
            'GET /api/coches/<id>': 'Obtener un coche por ID',
            'POST /api/coches': 'Crear un nuevo coche',
            'PUT /api/coches/<id>': 'Actualizar un coche',
            'DELETE /api/coches/<id>': 'Eliminar un coche'
        }
    })

# GET - Obtener todos los coches
@app.route('/api/coches', methods=['GET'])
def obtener_coches():
    try:
        coches = Coche.query.all()
        return jsonify([coche.to_dict() for coche in coches]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# GET - Obtener un coche por ID
@app.route('/api/coches/<int:id>', methods=['GET'])
def obtener_coche(id):
    try:
        coche = Coche.query.get(id)
        if coche:
            return jsonify(coche.to_dict()), 200
        return jsonify({'error': 'Coche no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# POST - Crear un nuevo coche
@app.route('/api/coches', methods=['POST'])
def crear_coche():
    try:
        datos = request.get_json()
        
        # Validar campos requeridos
        campos_requeridos = ['marca', 'modelo', 'año', 'precio', 'color']
        for campo in campos_requeridos:
            if campo not in datos:
                return jsonify({'error': f'El campo {campo} es requerido'}), 400
        
        # Crear nuevo coche
        nuevo_coche = Coche(
            marca=datos['marca'],
            modelo=datos['modelo'],
            año=datos['año'],
            precio=datos['precio'],
            color=datos['color']
        )
        
        db.session.add(nuevo_coche)
        db.session.commit()
        
        return jsonify(nuevo_coche.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# PUT - Actualizar un coche
@app.route('/api/coches/<int:id>', methods=['PUT'])
def actualizar_coche(id):
    try:
        coche = Coche.query.get(id)
        if not coche:
            return jsonify({'error': 'Coche no encontrado'}), 404
        
        datos = request.get_json()
        
        # Actualizar campos si están presentes
        if 'marca' in datos:
            coche.marca = datos['marca']
        if 'modelo' in datos:
            coche.modelo = datos['modelo']
        if 'año' in datos:
            coche.año = datos['año']
        if 'precio' in datos:
            coche.precio = datos['precio']
        if 'color' in datos:
            coche.color = datos['color']
        
        db.session.commit()
        
        return jsonify(coche.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# DELETE - Eliminar un coche
@app.route('/api/coches/<int:id>', methods=['DELETE'])
def eliminar_coche(id):
    try:
        coche = Coche.query.get(id)
        if not coche:
            return jsonify({'error': 'Coche no encontrado'}), 404
        
        db.session.delete(coche)
        db.session.commit()
        
        return jsonify({'mensaje': 'Coche eliminado correctamente'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
