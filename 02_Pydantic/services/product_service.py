from fastapi import HTTPException
from data.products import products
from schemas.products import ProductResponse, ProductCreate, ProductUpdate, ProductReplace

def get_all_products():
    return products


def create_new_products(product: ProductCreate):
    print(product)
    new_product = ProductResponse(
            id=len(products) + 1,
            name=product.name,
            price=product.price,
            category=product.category
        )
    
    products.append(new_product)
    
    return new_product



def update_product(
    product_id: int,
    product: ProductUpdate
):

    # Find the product
    for item in products:

        if item.id == product_id:

            # Get only fields sent by the client
            updated_data = product.model_dump(
                exclude_unset=True
            )

            # Update the fields
            for field, value in updated_data.items():
                setattr(item, field, value)

            return item

    # Product doesn't exist
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
    

def delete_product(product_id: int):

    # Find the product
    for item in products:

        if item.id == product_id:

            # Remove product from list
            products.remove(item)

            return {
                "message": "Product deleted",
                "product_id": product_id
            }

    # Product doesn't exist
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
 


def replace_product(
    product_id: int,
    product: ProductReplace
):

    # Find the existing product
    for index, item in enumerate(products):

        if item.id == product_id:

            # Replace the product
            updated_product = ProductResponse(
                id=product_id,
                name=product.name,
                price=product.price,
                category=product.category
            )

            products[index] = updated_product

            return updated_product

    # Product doesn't exist
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )