


from pydantic import BaseModel, Field, field_validator


class ProductTextMixin:
    @field_validator("name", "category", mode="before")
    @classmethod
    def clean_text_fields(cls, value):
        if value is None:
            return value

        if not isinstance(value, str):
            return value

        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("value cannot be blank")

        return cleaned_value


# Data required when creating a product
class ProductCreate(ProductTextMixin, BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    category: str = Field(min_length=2)


# Data allowed when partially updating a product
class ProductUpdate(ProductTextMixin, BaseModel):
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


class ProductReplace(ProductTextMixin, BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    category: str = Field(min_length=2)
