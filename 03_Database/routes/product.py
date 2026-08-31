
from fastapi import APIRouter, status, Depends
from services.product_service import get_all_products, create_product
from schemas.product import ProductCreate, ProductResponse
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductResponse])    
def get_products_router(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product_router(product:ProductCreate , db: Session = Depends(get_db)):
    return create_product(product , db)
 