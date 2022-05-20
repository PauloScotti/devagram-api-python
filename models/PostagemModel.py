from pydantic import BaseModel, Field
from typing import List

from models import ComentarioModel, UsuarioModel


class PostagemModel(BaseModel):
    id: str = Field(...)
    usuario: UsuarioModel = Field(...)
    foto: str = Filed(...)
    legenda: str = Filed(...)
    data: str = Filed(...)
    curtidas: int = Filed(...)
    comentarios: List[ComentarioModel] = Field(...)


class PostagemCriarModel(BaseModel):
        usuario: UsuarioModel = Field(...)
        foto: str = Filed(...)
        legenda: str = Filed(...)

    class Config:
        schema_extra = {
            "postagem": {
                "usuario": "UsuarioModel",
                "foto": "string",
                "legenda": "string"
            }
        }
