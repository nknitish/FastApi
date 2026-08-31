from fastapi import FastAPI
from routes.products import router as product_router

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "Welcome to Product Page"
    }


app.include_router(product_router)