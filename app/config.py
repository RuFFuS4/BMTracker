import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class Config:
    FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")
    PROJECT_ID = os.getenv("PROJECT_ID")
