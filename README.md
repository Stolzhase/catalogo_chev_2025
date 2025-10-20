# Catálogo de Coches - API REST con Flask

API REST desarrollada con Python y Flask para gestionar un catálogo de coches.

## Características

- ✅ CRUD completo (Crear, Leer, Actualizar, Eliminar)
- ✅ Base de datos SQLite con SQLAlchemy
- ✅ Modelo orientado a objetos
- ✅ Validación de datos
- ✅ CORS habilitado para integración con frontend
- ✅ Respuestas JSON estructuradas

## Modelo de Datos

Cada coche tiene los siguientes atributos:
- **Marca**: Fabricante del vehículo
- **Modelo**: Nombre del modelo
- **Año**: Año de fabricación
- **Precio**: Precio en la moneda local
- **Color**: Color del vehículo

## Instalación

1. Crear un entorno virtual:
\`\`\`bash
python -m venv venv
\`\`\`

2. Activar el entorno virtual:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

3. Instalar dependencias:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Ejecutar la aplicación:
\`\`\`bash
python app.py
\`\`\`

La API estará disponible en `http://localhost:5000`

## Endpoints de la API

### GET /api/coches
Obtiene todos los coches del catálogo.

**Respuesta:**
\`\`\`json
[
  {
    "id": 1,
    "marca": "Chevrolet",
    "modelo": "Silverado",
    "año": 2025,
    "precio": 45000.00,
    "color": "Negro",
    "fecha_creacion": "2025-01-19T10:30:00",
    "fecha_actualizacion": "2025-01-19T10:30:00"
  }
]
\`\`\`

### GET /api/coches/<id>
Obtiene un coche específico por su ID.

### POST /api/coches
Crea un nuevo coche en el catálogo.

**Body:**
\`\`\`json
{
  "marca": "Chevrolet",
  "modelo": "Camaro",
  "año": 2025,
  "precio": 55000.00,
  "color": "Rojo"
}
\`\`\`

### PUT /api/coches/<id>
Actualiza un coche existente.

**Body:**
\`\`\`json
{
  "precio": 52000.00,
  "color": "Azul"
}
\`\`\`

### DELETE /api/coches/<id>
Elimina un coche del catálogo.

## Estructura del Proyecto

\`\`\`
catalogo_chev_2025/
├── app.py              # Aplicación principal y rutas
├── models.py           # Modelo de datos (Coche)
├── config.py           # Configuración de la aplicación
├── requirements.txt    # Dependencias del proyecto
├── README.md          # Documentación
└── catalogo_coches.db # Base de datos SQLite (se crea automáticamente)
\`\`\`

## Tecnologías Utilizadas

- **Flask**: Framework web minimalista
- **SQLAlchemy**: ORM para manejo de base de datos
- **SQLite**: Base de datos ligera
- **Flask-CORS**: Soporte para peticiones cross-origin

## Próximos Pasos

- Agregar autenticación y autorización
- Implementar paginación para listados grandes
- Agregar filtros de búsqueda (por marca, año, rango de precio)
- Crear un frontend para consumir la API
- Agregar imágenes de los coches
- Implementar tests unitarios
