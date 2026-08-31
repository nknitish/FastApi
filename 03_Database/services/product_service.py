from schemas.product import ProductCreate
from models.product import Product
from sqlalchemy.orm import Session

def get_all_products(db: Session):
    return db.query(Product).all()

def create_product(product:ProductCreate, db:Session):
    new_product = Product(
        name=product.name,
        price=product.price,
        category=product.category
    )
    
    # Add product to the database session
    db.add(new_product)
    
    # Save the changes to the database
    db.commit()
    
    #Get the generated ID and other DB values
    db.refresh(new_product)
    
    return new_product
