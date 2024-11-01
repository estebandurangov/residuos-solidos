from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.router import router

def create_app():
    app = FastAPI()
    app.include_router(router)
    return app

app = create_app()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow requests from this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)