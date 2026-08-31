from fastapi import FastAPI

app = FastAPI()


# ============================================================
# Simple in-memory database
# ============================================================

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 20000},
    {"id": 3, "name": "Keyboard", "price": 1500}
]


# ============================================================
# GET - Get all products
#
# Query Parameter:
# /products?limit=2
# ============================================================

@app.get("/products")
def get_products(limit: int = 5):

    return {
        "limit": limit,
        "data": products[:limit]
    }


# ============================================================
# GET - Get one product
#
# Path Parameter:
# /products/1
# ============================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {
        "message": "Product not found"
    }


# ============================================================
# POST - Create a new product
#
# URL:
# /products
#
# Query Parameters:
# /products?name=Mouse&price=800
# ============================================================

@app.post("/products")
def create_product(name: str, price: float):
   
    new_id = len(products) + 1

    new_product = {
        "id": new_id,
        "name": name,
        "price": price
    }

    # Add product to list
    products.append(new_product)

    return {
        "message": "Product created successfully",
        "data": new_product
    }


# ============================================================
# PUT - Update a product
#
# Path Parameter:
# /products/1
#
# Query Parameters:
# /products/1?name=Gaming Laptop&price=75000
# ============================================================

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    name: str,
    price: float
):

    for product in products:

        if product["id"] == product_id:

            # Update product
            product["name"] = name
            product["price"] = price

            return {
                "message": "Product updated successfully",
                "data": product
            }

    return {
        "message": "Product not found"
    }


# ============================================================
# DELETE - Delete a product
# ============================================================

@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for product in products:

        if product["id"] == product_id:

            # Remove product from list
            products.remove(product)

            return {
                "message": "Product deleted successfully",
                "data": product
            }

    return {
        "message": "Product not found"
    }