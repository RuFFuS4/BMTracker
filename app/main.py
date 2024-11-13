from fasthtml import FastHTML
from app.routes import markers
from app.services.firebase import initialize_firebase
from app.middleware.auth_middleware import auth_middleware


# Inicializar la aplicación de FastHTML
app = FastHTML()

# Inicializar Firebase
initialize_firebase()

# Registrar rutas
app.include_router(markers.router)

app.add_middleware(auth_middleware)

if __name__ == "__main__":
    app.run()
