import firebase_admin
from firebase_admin import credentials, firestore, auth
from app.config import Config

# Inicializar Firebase
def initialize_firebase():
    cred = credentials.Certificate("path/to/your-firebase-credentials.json")
    firebase_admin.initialize_app(cred)

# Conexión a Firestore
db = firestore.client()

# Función para verificar el token de usuario
def verify_user_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token
    except Exception as e:
        return None

# Función para agregar un marcador
def add_marker(marker_data):
    db.collection("marcadores").add(marker_data)
    return {"message": "Marcador agregado"}

# Función para obtener todos los marcadores
def get_markers():
    markers = db.collection("marcadores").stream()
    return [{"id": marker.id, **marker.to_dict()} for marker in markers]

# Función para actualizar un marcador
def update_marker(marker_id, marker_data):
    db.collection("marcadores").document(marker_id).update(marker_data)
    return {"message": "Marcador actualizado"}

# Función para eliminar un marcador
def delete_marker(marker_id):
    db.collection("marcadores").document(marker_id).delete()
    return {"message": "Marcador eliminado"}
