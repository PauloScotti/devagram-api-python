from fastapi import APIRouter, Body

from models.UsuarioModel import UsuarioModel
from repositories.UsuarioRepository import criar_usuario

router = APIRouter()


@router.post("/", response_description="Rota para criar novo usuário")
async def rota_criar_usuario(usuario: UsuarioModel = Body(...)):
    resultado = await criar_usuario(usuario)

    return resultado
