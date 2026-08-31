
from fastapi import FastAPI;
from database import engine, Base
from models.product import Product
from routes.product import router as product_router

app= FastAPI()



# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"Message":"Hello World"}


app.include_router(product_router)