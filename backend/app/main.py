import os
import sys

# Inject project root and app directory into sys.path to guarantee import resolution
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)
sys.path.insert(0, current_dir)

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from database.db import engine
from models import Base
from routes import auth, users, learning, jobs, routine, health
import uvicorn

# Automatically initialize database schema tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Neuro-Assist API",
    description="Unified API server supporting personalized learning, employment, routines, and health tracking.",
    version="1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(auth.auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users.users_router, prefix="/users", tags=["Users"])
app.include_router(learning.learning_router, prefix="/learning", tags=["Learning Assistance"])
app.include_router(jobs.jobs_router, prefix="/jobs", tags=["Employment Support"])
app.include_router(routine.routine_router, prefix="/routine", tags=["Routine Management"])
app.include_router(health.health_router, prefix="/health", tags=["Mental Health Monitoring"])


# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Neuro-Assist API (Unified & Operational)"}


# Run the application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
