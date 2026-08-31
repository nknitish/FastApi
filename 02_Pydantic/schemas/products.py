


from pydantic import BaseModel, Field


# Data required when creating a product
class ProductCreate(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    category: str = Field(min_length=2)


# Data allowed when partially updating a product
class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = Field(
        default=None,
        gt=0
    )
    category: str | None = None


# Data returned by the API
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category: str
    

class ProductReplace(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    category: str = Field(min_length=2)
    