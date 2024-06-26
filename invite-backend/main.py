from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import operation
from database.db import engine, Base


app = FastAPI()

origins = [
    "https://iinve.com",     # Your frontend domain
    "https://www.iinve.com", # Optional: www subdomain for your frontend
    "https://api.iinve.com", # Your backend domain
    "https://www.api.iinve.com", # Your backend domain
    "http://localhost:8000", 
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(operation.router)


Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)