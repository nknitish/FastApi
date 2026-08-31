from fastapi import APIRouter, HTTPException, status
from services.product_service import get_all_products, create_new_products, update_product,delete_product, replace_product

from schemas.products import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductReplace
)

from data.products import products


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


# -------------------------
# GET all products
# -------------------------

@router.get(
    "/",
    response_model=list[ProductResponse]
)
def get_products_route():
    return get_all_products()


# -------------------------
# CREATE product
# -------------------------

@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product_route(product: ProductCreate):
    return create_new_products(product)


# -------------------------
# UPDATE product
# -------------------------

@router.patch(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product_route(
    product_id: int,
    product: ProductUpdate
):
    return update_product(product_id, product)

    

# -------------------------
# DELETE product
# -------------------------

@router.delete("/{product_id}")
def delete_product_route(product_id: int):
    return delete_product(product_id)


# -------------------------
# PUT product
# -------------------------    

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def replace_product_route(
    product_id: int,
    product: ProductReplace
): 
    return replace_product(product_id, product)