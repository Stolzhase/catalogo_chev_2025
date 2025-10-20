"""
Script para poblar la base de datos con datos de ejemplo
"""
from app import app, db
from models import Coche

def seed_database():
    with app.app_context():
        # Limpiar la base de datos
        db.drop_all()
        db.create_all()
        
        # Datos de ejemplo de coches Chevrolet 2025
        coches_ejemplo = [
            Coche(
                marca="Chevrolet",
                modelo="Silverado 1500",
                año=2025,
                precio=45000.00,
                color="Negro"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Camaro SS",
                año=2025,
                precio=55000.00,
                color="Rojo"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Corvette Z06",
                año=2025,
                precio=125000.00,
                color="Amarillo"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Tahoe",
                año=2025,
                precio=65000.00,
                color="Blanco"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Equinox",
                año=2025,
                precio=35000.00,
                color="Gris"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Blazer",
                año=2025,
                precio=42000.00,
                color="Azul"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Trailblazer",
                año=2025,
                precio=28000.00,
                color="Verde"
            ),
            Coche(
                marca="Chevrolet",
                modelo="Suburban",
                año=2025,
                precio=75000.00,
                color="Negro"
            )
        ]
        
        # Agregar todos los coches a la base de datos
        for coche in coches_ejemplo:
            db.session.add(coche)
        
        db.session.commit()
        
        print(f"✅ Base de datos poblada con {len(coches_ejemplo)} coches de ejemplo")
        print("\nCoches agregados:")
        for coche in coches_ejemplo:
            print(f"  - {coche.marca} {coche.modelo} ({coche.año}) - ${coche.precio:,.2f} - {coche.color}")

if __name__ == '__main__':
    seed_database()
