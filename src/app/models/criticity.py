from pydantic import BaseModel, Field, field_validator

class Criticity(BaseModel):
    name: str = Field(
        description="Nombre de la criticidad",
        examples=["Importante", "Crítico", "Urgente"],
        min_length=2,
        max_length=100
    )

    @field_validator("name")
    @classmethod
    def clean_name(cls, v: str) -> str:
        return v.strip()