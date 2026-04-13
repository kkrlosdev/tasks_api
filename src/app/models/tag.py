from pydantic import BaseModel, Field, field_validator

class Tag(BaseModel):
    name: str = Field(
        description="Nombre del tag",
        examples=["TODO", "Tech", "Friki"],
        min_length=1,
        max_length=100
    )

    @field_validator("name")
    @classmethod
    def clean_name(cls, v: str) -> str:
        return v.strip()